from flask_restx import Namespace, Resource, fields

from enums.stemming import SnowBallStemmerLanguageEnum
from handlers.tokenizer import TokenizerHandler
from handlers.stemming import SnowballStemmerHandler
from models.stemming import StemmingModel

api = Namespace('stemmer', description='Gets the root of sentence words')

input_model = api.model('SentencesToStem', {
    'sentences' : fields.List(fields.String(), required=True, default=["I'm trying to explain a feature", "I was trying to explain some features"], description='A list of sentences which words will be stemmed')
})

output_model = api.model('StemmedWordSentences', {
    'sentences' : fields.List(fields.String(), required=True, default=["sentence with stemmed words 1", "sentence with stemmed words 2"], description='A list of sentences which words have been stemmed')
})

@api.param('language', 'The language of the sentences', enum = SnowBallStemmerLanguageEnum._member_names_)
class SnowballStemmerResource(Resource):
    @api.expect(input_model)
    @api.marshal_with(output_model)
    def post(self,language):
        sentences = api.payload["sentences"]
        
        tokenizer = TokenizerHandler() 
        stemmer = SnowballStemmerHandler(SnowBallStemmerLanguageEnum[language])
        
        out = StemmingModel()
        for sentence in sentences:
            out.sentences.append(str.join(' ',[stemmer.Handle(word) for word in tokenizer.GetWords(sentence)]))

        return out


api.add_resource(SnowballStemmerResource, '/stem/snowball/<string:language>')