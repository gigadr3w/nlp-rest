from flask_restx import Namespace, Resource, fields
from nltk import word_tokenize

from enums.correctors import CorrectorLanguageEnum
from models.corrector import CorrectionModel

from handlers.corrector import CorrectorHandler

api = Namespace('corrector', description='Using pyEnchant, corrects an entire sentence for the selected language')

input_model = api.model('ToCorrect', {
    'sentences' : fields.List(fields.String(), required=True, description='The sentence that have to been corrected') 
})

output_model = api.model('Corrected', {
    'sentences' : fields.String(description='The correct sentence') 
})

@api.route('/corrector/<string:language>')
@api.param('language', description='The language to consider to correct the sentence', enum=CorrectorLanguageEnum._member_names_)
class CorrectorResource(Resource):
    @api.expect(input_model)
    @api.marshal_with(output_model)
    def post(self, language):
        corrector_handler = CorrectorHandler(CorrectorLanguageEnum[language])
        sentences = api.payload['sentences']

        out = CorrectionModel()
        
        for sentence in sentences:
            #check if each word is semantically corrected and if not suggest a correction
            corrected_words = [corrector_handler.Handle(word) for word in word_tokenize(sentence)]
            out.sentences.append(str.join(' ', corrected_words))
        
        return out