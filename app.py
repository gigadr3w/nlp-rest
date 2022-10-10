import sys, logging
from flask import Flask
from flask_restx import Api
from waitress import serve

from handlers.corrector import InitCorrectors
from handlers.stemming import InitSnowballStemmers
from handlers.spacy import InitSpacyAsync

from api.corrector import api as api_corrector
from api.tokenizer import api as api_tokenizer
from api.stemming import api as api_stemming
from api.lemmatize import api as api_lemmatizer

version = "1.0.1"

app = Flask(__name__)
api = Api()

api.init_app(app, version=version, title='Natural Language Processing API', description='Some NLP methods to process sentences!')

api.add_namespace(api_corrector, path='/api')
api.add_namespace(api_tokenizer, path='/api')
api.add_namespace(api_stemming, path='/api')
api.add_namespace(api_lemmatizer, path='/api')

app.config['JSON_AS_ASCII'] = False

args = sys.argv

def init():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')
    InitCorrectors()
    InitSnowballStemmers()
    InitSpacyAsync()


if(__name__ == "__main__"):
    init()

    if len(args) > 1 and args[1] == "prod":
        logging.info('PRODUCTION ENVIRONMENT')
        serve(app, port="8087")
    else:
        logging.info('DEVELOPMENT ENVIRONMENT')
        app.run(debug=True, port="8087")

