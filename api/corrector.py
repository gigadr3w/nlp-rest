from email.policy import default
from flask_restx import Namespace, Resource, fields, reqparse
from nltk import word_tokenize

from enums.correctors import CorrectorLanguageEnum
from models.corrector import CorrectionModel

from handlers.corrector import CorrectorHandler

api = Namespace('corrector', description='Corrects sentences words')

parser = reqparse.RequestParser()
parser.add_argument('sentences', required=True, action='append', help='The sentences that have to been corrected', location='args')

output_model = api.model('CorrectedSentences', {
    'sentences' : fields.List(fields.String(), required=True, default=['corrected sentence 1', 'corrected sentence 2'], description='The correct sentences') 
})

@api.route('/correct/<string:language>')
@api.param('language', description='The language of the sentence', enum=CorrectorLanguageEnum._member_names_)
class CorrectorResource(Resource):
    @api.expect(parser)
    @api.marshal_with(output_model)
    def get(self, language):
        corrector_handler = CorrectorHandler(CorrectorLanguageEnum[language])
        sentences = parser.parse_args()['sentences']

        out = CorrectionModel()
        
        for sentence in sentences:
            #check if each word is semantically corrected and if not suggest a correction
            corrected_words = [corrector_handler.Handle(word) for word in word_tokenize(sentence)]
            out.sentences.append(str.join(' ', corrected_words))
        
        return out