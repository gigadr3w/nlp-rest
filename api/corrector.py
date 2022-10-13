from flask_restx import Namespace, Resource, fields
from nltk import word_tokenize

from enums.correctors import CorrectorLanguageEnum
from models.corrector import CorrectionModel

from handlers.corrector import CorrectorHandler

api = Namespace('corrector', description='Using pyEnchant, corrects a list of sentences')

input_model = api.model('SentencesToCorrect ', {
    'sentences' : fields.List(fields.String(), required=True, default=['semtence to correct 1', 'sentence to corect 2'], description='The sentences that have to been corrected') 
})

output_model = api.model('CorrectedSentences', {
    'sentences' : fields.List(fields.String(), required=True, default=['corrected sentence 1', 'corrected sentence 2'], description='The correct sentences') 
})

@api.route('/correct/<string:language>')
@api.param('language', description='The language of the sentence', enum=CorrectorLanguageEnum._member_names_)
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