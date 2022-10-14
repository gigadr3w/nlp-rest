from flask_restx import Resource, Namespace, fields

from enums.spacy import SpacyLanguageEnum
from handlers.ner import SpacyNERHandler

api = Namespace('named entity recognition', description='Recognizes named entity such as organizations, countries, dates. Note - not all spacy dictionaries may recognize some entities')

input_model = api.model('SentenceToCheckForNER', {
    'sentence' : fields.String(required=True, default="Aristotele was born in Stagira, 384 a.C. . He was one of the most important phylosopher and Alessandro Magno was its disciple. Tomorrow there's an event about it, it costs about 20 pounds.", description='The sentence from which we want to extract its named entities')
})

output_model = api.model('NERFoundList', {
    'text' : fields.String(required=True, description='The current word as simple text'),
    'start' : fields.Integer(required=True, description='The current word position start within the sentence'),
    'end' : fields.Integer(required=True, description='The current word position end within the sentence'),
    'entity' : fields.String(required=True, description='The entity name')
})

@api.route('/ner/<string:language>')
@api.param('language', 'The language of the sentence', enum = SpacyLanguageEnum._member_names_)
class SpacyNERResource(Resource):
    @api.expect(input_model)
    @api.marshal_list_with(output_model)
    def post(self, language):
        handler = SpacyNERHandler(SpacyLanguageEnum[language])
        sentence = api.payload['sentence']
        return handler.NamedEntityRecognition(sentence)