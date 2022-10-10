from flask_restx import Namespace, Resource, fields

from enums.stemming import SnowBallStemmerLanguageEnum
from handlers.tokenizer import TokenizerHandler
from handlers.stemming import SnowballStemmerHandler
from models.stemming import StemmingModel

api = Namespace('stemmer', description='Use NLTK SnowballStemmer algorithm to stem sentences words')

input_model = api.model('ToStem', {
    'sentences' : fields.List(fields.String(), required=True, default=["sentence1", "sentence2"], description='A list of sentences which words will be stemmed')
})

output_model = api.model('Stemmed', {
    'sentences' : fields.List(fields.String(), required=True, default=["sentence1 with stemmed word", "sentence1 with stemmed word"], description='A list of sentences which words have been stemmed')
})

@api.param('language', 'The language of the stemmer dictionary used to stem words (it must equal to the sentences language)', enum = SnowBallStemmerLanguageEnum._member_names_)
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