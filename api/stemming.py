from flask_restx import Namespace, Resource, fields, reqparse

from enums.stemming import SnowBallStemmerLanguageEnum
from handlers.tokenizer import TokenizerHandler
from handlers.stemming import SnowballStemmerHandler
from models.stemming import StemmingModel

api = Namespace('stemmer', description='Gets the root of sentence words')

parser = reqparse.RequestParser()
parser.add_argument('sentences', required=True, location='args', action='append', help='A list of sentences which words will be stemmed')

output_model = api.model('StemmedWordSentences', {
    'sentences' : fields.List(fields.String(), required=True, default=["sentence with stemmed words 1", "sentence with stemmed words 2"], description='A list of sentences which words have been stemmed')
})

@api.param('language', 'The language of the sentences', enum = SnowBallStemmerLanguageEnum._member_names_)
class SnowballStemmerResource(Resource):
    @api.expect(parser)
    @api.marshal_with(output_model)
    def get(self,language):
        sentences = parser.parse_args()["sentences"]
        
        tokenizer = TokenizerHandler() 
        stemmer = SnowballStemmerHandler(SnowBallStemmerLanguageEnum[language])
        
        out = StemmingModel()
        for sentence in sentences:
            out.sentences.append(str.join(' ',[stemmer.Handle(word) for word in tokenizer.GetWords(sentence)]))

        return out


api.add_resource(SnowballStemmerResource, '/stem/snowball/<string:language>')