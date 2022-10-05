from flask_restx import Namespace, Resource, fields
from nltk import word_tokenize

from enums.correctors import CorrectorLanguageEnum
from models.correction import CorrectionModel

from nlp.corrector import Correctors

api = Namespace('corrector', description='Method that correct an entire sentence due to the specified languages')

input_model = api.model('ToCorrect', {
    'sentences' : fields.List(fields.String(), required=True, description='The sentence that have to been corrected') 
})

output_model = api.model('Corrected', {
    'sentences' : fields.String(description='The correct sentence') 
})

def suggest(language:CorrectorLanguageEnum, word:str) -> str:
    #Suggest the first most reliable term for the wrong word passed as argument 
    try:
        return Correctors(language).suggest(word)[0]
    except:
        return word

@api.route('/corrector/<string:language>')
@api.param('language', description='The language of the dictionary with which correct the sentence', enum=CorrectorLanguageEnum._member_names_)
class CorrectorResource(Resource):
    @api.expect(input_model)
    @api.marshal_with(output_model)
    def post(self, language):
        corrector_language = CorrectorLanguageEnum[language]
        sentences = api.payload['sentences']

        out = CorrectionModel()
        
        for sentence in sentences:
            #check if each word is semantically corrected and if not suggest a correction
            corrected_words = [suggest(corrector_language,word) if not Correctors[corrector_language].check(word) else word for word in word_tokenize(sentence)]
            out.sentences.append(str.join(' ', corrected_words))
        
        return out