import sys, logging
from flask import Flask
from flask_restx import Api
from waitress import serve

from factories.enchant import InitEnchantDictionaries
from factories.snowballstemmer import InitSnowballStemmers
from factories.spacy import InitSpacyAsync

from api.corrector import api as api_corrector
from api.tokenizer import api as api_tokenizer
from api.stemming import api as api_stemming
from api.lemmatize import api as api_lemmatizer
from api.named_entity_recognition import api as api_ner
from api.deep_analysis import api as api_analysis

version = "1.0.1"

app = Flask(__name__)
api = Api()

api.init_app(app, version=version, title='Natural Language Processing API', description='Some NLP methods to process sentences!')

api.add_namespace(api_corrector, path='/api')
api.add_namespace(api_tokenizer, path='/api')
api.add_namespace(api_stemming, path='/api')
api.add_namespace(api_lemmatizer, path='/api')
api.add_namespace(api_ner, path='/api')
api.add_namespace(api_analysis, path='/api')

app.config['JSON_AS_ASCII'] = False

args = sys.argv

def init():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')
    InitEnchantDictionaries()
    InitSnowballStemmers()
    InitSpacyAsync()


if(__name__ == "__main__"):
    init()

    if len(args) > 1 and args[1] == "prod":
        logging.info('PRODUCTION ENVIRONMENT')
        serve(app, port="5000")
    else:
        logging.info('DEVELOPMENT ENVIRONMENT')
        app.run(debug=True, port="5000")

