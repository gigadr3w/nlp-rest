from flask_restx import Namespace, Resource, fields
from flask import jsonify

from models.tokenizer import TokenizationModel
from handlers.tokenizer import TokenizerHandler

api = Namespace('tokenizer', description='Using NLTK library, tokenizes a sentence into an array of words or a sentences in a list of sentence')

input_model = api.model('ToTokenize', {
    'sentence' : fields.String(required=True, default='The sentence we want tokenize', description='The sentence that will be tokenized')
})

output_model = api.model('Tokenized', {
    'tokens' : fields.List(fields.String(), required=True, default=["token1", "token2"], description='Due to the handled endpoint, a list of words or a list of sentences')
})

class TokenizeWordsResource(Resource):
    @api.expect(input_model)
    @api.marshal_with(output_model)
    def post(self):
        out = TokenizationModel()
        handler = TokenizerHandler()
        out.tokens = handler.GetWords(api.payload['sentence'])
        return out

class TokenizeSentencesResource(Resource):
    @api.expect(input_model)
    @api.marshal_with(output_model)
    def post(self):
        out = TokenizationModel()
        handler = TokenizerHandler()
        out.tokens = handler.GetStatements(api.payload['sentence'])
        return out

api.add_resource(TokenizeWordsResource, '/tokenize/words')
api.add_resource(TokenizeSentencesResource, '/tokenize/sentences')