import sys, logging
from flask import Flask
from flask_restx import Api
from waitress import serve

from handlers.corrector import InitCorrectors
from handlers.stemming import InitSnowballStemmers

from api.corrector import api as api_corrector
from api.tokenizer import api as api_tokenizer
from api.stemming import api as api_stemming

version = "1.0.1"

app = Flask(__name__)
api = Api()

api.init_app(app, version=version, title='Natural Language Processing API', description='Some NLP methods to process sentences!')

api.add_namespace(api_corrector, path='/api')
api.add_namespace(api_tokenizer, path='/api')
api.add_namespace(api_stemming, path='/api')

app.config['JSON_AS_ASCII'] = False

args = sys.argv

# @api.route("/about")
# def about():
#     return "<p>Hi everybody, this is the <b>Nlp REST Api</b> " + version + " service</p>"

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

# def suggest(language, word):
#     try:
#         return correctors[language].suggest(word)[0]
#     except:
#         return str()

# def initLemmantizer(language, dictionary):
#     lemmatizers[language] = spacy.load(dictionary)
#     logging.debug("spaCy loaded " + dictionary + " dataset for " + language + " language.")

# def initLemmatizers():
#     with concurrent.futures.ThreadPoolExecutor(max_workers=len(SpacyDictionaries)) as executor:
#         for d in SpacyDictionaries:
#             executor.submit(initLemmantizer, d[0], d[1])
#     logging.info("Lemmatizers are ready!")


def init():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')
    InitCorrectors()
    InitSnowballStemmers()

if(__name__ == "__main__"):
    init()

    if len(args) > 1 and args[1] == "prod":
        logging.info('PRODUCTION ENVIRONMENT')
        serve(app, port="8087")
    else:
        logging.info('DEVELOPMENT ENVIRONMENT')
        app.run(debug=True, port="8087")

