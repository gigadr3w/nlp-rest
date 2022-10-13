from flask_restx import Namespace, Resource, fields

from enums.stemming import SnowBallStemmerLanguageEnum
from handlers.tokenizer import TokenizerHandler
from handlers.stemming import SnowballStemmerHandler
from models.stemming import StemmingModel

api = Namespace('stemmer', description='Use NLTK SnowballStemmer algorithm to stem sentences words')

input_model = api.model('SentencesToStem', {
    'sentences' : fields.List(fields.String(), required=True, default=["sentence to stem", "stemming sentences"], description='A list of sentences which words will be stemmed')
})

output_model = api.model('StemmedSentences', {
    'sentences' : fields.List(fields.String(), required=True, default=["sentence1 with stemmed word", "sentence1 with stemmed word"], description='A list of sentences which words have been stemmed')
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