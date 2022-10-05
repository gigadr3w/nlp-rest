import sys, spacy, enchant, concurrent.futures, logging
#from enums import SpacyDictionaries, SnowballStemmerLanguages, EnchantLanguages
from nltk.stem import SnowballStemmer 
from nltk import RegexpTokenizer
from flask import Flask, request, json
from flask_restx import Resource, Api
from waitress import serve
from werkzeug.exceptions import abort

from api.about import api as api_about
from api.corrector import api as api_corrector

version = "1.0.1"

api = Api()

api.add_namespace(api_corrector, path='/api')

app = Flask(__name__)
api.init_app(app, version=version, title='Natural Language Processing API', description='Some cool methods to process statements!')

app.config['JSON_AS_ASCII'] = False

args = sys.argv

lemmatizers = dict()
stemmers = dict()
correctors = dict()

# @api.route("/about")
# def about():
#     return "<p>Hi everybody, this is the <b>Nlp REST Api</b> " + version + " service</p>"

# def evaluate_request_utterances(request):
#     utterances = list()
#     if request.method == "GET" and "utterance" not in request.values.keys():
#         msg = "HTTP GET request must have a 'utterance' argument!"
#         logging.warning(msg)
#         abort(400, msg)
#     elif request.method == "GET":
#         utterances.append(request.values["utterance"])

#     if request.method == "POST" and request.get_json() is None:
#         msg = "Http lemmantize POST request must have a string array as json parameter!"
#         logging.warning(msg)
#         abort(400, msg)
#     elif request.method == "POST":
#         utterances = request.get_json()

#     return utterances

# @api.route("/<string:language>/lemmatize", methods = ["GET", "POST"])
# def lemmatize(language):
#     results = list()
#     if not language in lemmatizers.keys():
#         msg = "Sorry, but " + language + " was not found in lemmantizers aivaiable languages"
#         logging.warning(msg)
#         abort(500, msg)

#     utterances = evaluate_request_utterances(request)

#     for utterance in utterances:
#         words = lemmatizers[language](utterance)
#         results.append(str.join(' ', [word.lemma_ for word in words]))

#     return json.jsonify(results)

# @api.route("/<string:language>/stemming", methods = ["GET", "POST"])
# def stemming(language):
#     results = list()
#     if not language in stemmers.keys():
#         msg = "Sorry, but " + language + " was not found in lemmantizers aivaiable languages"
#         logging.warning(msg)
#         abort(500, msg)

#     utterances = evaluate_request_utterances(request)
#     #only words
#     tokenizer = RegexpTokenizer(r'\w+')
#     for utterance in utterances:
#         results.append(str.join(' ', [stemmers[language].stem(word) for word in tokenizer.tokenize(utterance)]))

#     return json.jsonify(results)

# def suggest(language, word):
#     try:
#         return correctors[language].suggest(word)[0]
#     except:
#         return str()

# @api.route("/<string:language>/correct", methods = ["GET", "POST"])
# def correct(language):
#     results = list()
#     if not language in stemmers.keys():
#         msg = "Sorry, but " + language + " was not found in lemmantizers aivaiable languages"
#         logging.warning(msg)
#         abort(500, msg)

#     utterances = evaluate_request_utterances(request)
#     #only words
#     tokenizer = RegexpTokenizer(r'\w+')
#     for utterance in utterances:
#         results.append(str.join(' ', [suggest(language,word) if not correctors[language].check(word) else word for word in tokenizer.tokenize(utterance)]))

#     return json.jsonify(results)

# def initLemmantizer(language, dictionary):
#     lemmatizers[language] = spacy.load(dictionary)
#     logging.debug("spaCy loaded " + dictionary + " dataset for " + language + " language.")

# def initLemmatizers():
#     with concurrent.futures.ThreadPoolExecutor(max_workers=len(SpacyDictionaries)) as executor:
#         for d in SpacyDictionaries:
#             executor.submit(initLemmantizer, d[0], d[1])
#     logging.info("Lemmatizers are ready!")

# def initStemmers():
#     for l in SnowballStemmerLanguages:
#         stemmers[l[0]] = SnowballStemmer(l[1])
#         logging.debug("SnowballStemmer loaded for " + l[0] + " language.")
#     logging.info("Stemmers are ready!")

# def initCorrector():
#     for l in EnchantLanguages:
#         correctors[l[0]] = enchant.Dict(l[1])
#         logging.debug("Enchant load " + l[1] + " dictionary for " + l[0] + " language.")
#     logging.info("Correctors are ready!")


def init():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')
    # initLemmatizers()
    # initStemmers()
    # initCorrector()

if(__name__ == "__main__"):
    init()

    if len(args) > 1 and args[1] == "prod":
        logging.info('PRODUCTION ENVIRONMENT')
        serve(app, port="8087")
    else:
        logging.info('DEVELOPMENT ENVIRONMENT')
        app.run(debug=True, port="8087")

