from flask_restx import Resource, Namespace, fields
from langcodes import Language

from enums.spacy import SpacyLanguageEnum
from models.named_entity_recognition import NamedEntityRecognitionModel
from handlers.spacy import SpacyHandler

api = Namespace('named entity recognition', description='Recognizes named entity such as Organizations, Countries, Names...')

input_model = api.model('ToNamedEntityRecognitionCheck', {
    'sentence' : fields.String(required=True, description='The sentence from which we want to extract Named Entities')
})

output_model = api.model('EntityNameRecognitionList', {
    'text' : fields.String(required=True, description='The current word as simple text'),
    'start' : fields.Integer(required=True, description='The current word position start within the sentence'),
    'end' : fields.Integer(required=True, description='The current word position end within the sentence'),
    'entity' : fields.String(required=True, description='The entity name')
})

@api.route('/ner/<string:language>')
@api.param('language', 'The language of the spacy dictionary used to lemmatize words (it must equal to the sentences language)', enum = SpacyLanguageEnum._member_names_)
class SpacyNERResource(Resource):
    @api.expect(input_model)
    @api.marshal_list_with(output_model)
    def post(self, language):
        handler = SpacyHandler(SpacyLanguageEnum[language])
        sentence = api.payload['sentence']
        return handler.GetNER(sentence)