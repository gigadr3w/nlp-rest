from flask_restx import Resource, Namespace, fields, reqparse
from numpy import require

from enums.spacy import SpacyLanguageEnum
from handlers.ner import SpacyNERHandler

api = Namespace('named entity recognition', description='Recognizes named entity such as organizations, countries, dates. Note - not all spacy dictionaries may recognize some entities')

parser = reqparse.RequestParser()
parser.add_argument('sentence', required=True, location='args', help='The sentence from which we want to extract its named entities')

output_model = api.model('NERFoundList', {
    'text' : fields.String(required=True, description='The current word as simple text'),
    'start' : fields.Integer(required=True, description='The current word position start within the sentence'),
    'end' : fields.Integer(required=True, description='The current word position end within the sentence'),
    'entity' : fields.String(required=True, description='The entity name')
})

@api.route('/ner/<string:language>')
@api.param('language', 'The language of the sentence', enum = SpacyLanguageEnum._member_names_)
class SpacyNERResource(Resource):
    @api.expect(parser)
    @api.marshal_list_with(output_model)
    def get(self, language):
        handler = SpacyNERHandler(SpacyLanguageEnum[language])
        sentence = parser.parse_args()['sentence']
        out = handler.NamedEntityRecognition(sentence)
        return out