from flask_restx import Namespace, Resource, fields

from models.tokenizer import TokenizationModel
from handlers.tokenizer import TokenizerHandler

api = Namespace('tokenizer', description='Using NLTK library, tokenizes a sentence into an array of words or a sentences in a list of sentence')

input_model = api.model('SentencesToTokenize', {
    'sentences' : fields.List(fields.String(), required=True, description='The sentence we want tokenize', default=["sentence to tokenize1", "sentence to tokenize2"],)
})

output_model = api.model('TokenizedSentences', {
    'sentence' : fields.String(required=True, description='The input sentence'),
    'tokens' : fields.List(fields.String(), required=True, default=["token1", "token2"], description='Due to the handled endpoint, a list of words or a list of sentences')
})

class TokenizeWordsResource(Resource):
    @api.expect(input_model)
    @api.marshal_list_with(output_model)
    def post(self):
        out = list()
        handler = TokenizerHandler()

        sentences = api.payload['sentences']
        for sentence in sentences:
            item = TokenizationModel()
            item.sentence = sentence
            item.tokens = handler.GetWords(sentence)
            out.append(item)

        return out

class TokenizeSentencesResource(Resource):
    @api.expect(input_model)
    @api.marshal_list_with(output_model)
    def post(self):
        out = list()
        handler = TokenizerHandler()

        sentences = api.payload['sentences']
        for sentence in sentences:
            item = TokenizationModel()
            item.sentence = sentence
            item.tokens = handler.GetStatements(sentence)
            out.append(item)
            
        return out

api.add_resource(TokenizeWordsResource, '/tokenize/words')
api.add_resource(TokenizeSentencesResource, '/tokenize/sentences')