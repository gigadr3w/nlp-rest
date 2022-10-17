from flask_restx import Namespace, Resource, fields, reqparse
from numpy import require

from models.tokenizer import TokenizationModel
from handlers.tokenizer import TokenizerHandler

api = Namespace('tokenizer', description='Tokenizes a sentence into an array of words or a sentences in a list of sentence')

parser = reqparse.RequestParser()
parser.add_argument('sentences', required=True, location='args', action='append', help='The sentence we want tokenize')

output_model = api.model('TokenizedSentences', {
    'sentence' : fields.String(required=True, description='The input sentence'),
    'tokens' : fields.List(fields.String(), required=True, default=["token1", "token2"], description='Due to the handled endpoint, a list of words or a list of sentences')
})

class TokenizeWordsResource(Resource):
    @api.expect(parser)
    @api.marshal_list_with(output_model)
    def get(self):
        out = list()
        handler = TokenizerHandler()

        sentences = parser.parse_args()['sentences']
        for sentence in sentences:
            item = TokenizationModel()
            item.sentence = sentence
            item.tokens = handler.GetWords(sentence)
            out.append(item)

        return out

class TokenizeSentencesResource(Resource):
    @api.expect(parser)
    @api.marshal_list_with(output_model)
    def get(self):
        out = list()
        handler = TokenizerHandler()

        sentences = parser.parse_args()['sentences']
        for sentence in sentences:
            item = TokenizationModel()
            item.sentence = sentence
            item.tokens = handler.GetStatements(sentence)
            out.append(item)
            
        return out

api.add_resource(TokenizeWordsResource, '/tokenize/words')
api.add_resource(TokenizeSentencesResource, '/tokenize/sentences')