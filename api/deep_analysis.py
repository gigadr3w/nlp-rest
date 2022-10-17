from flask_restx import Namespace, fields, Resource, reqparse

from enums.sentence_analysis import DeepAnalyzerLanguageEnum
from enums.pos import POSTypeEnum
from enums.text_type import TextTypeEnum

from handlers.deep_analyzer import DeepAnalyzerHandler 

api = Namespace('sentence deep analysis', description='Returns deep analysis details such as part-of-speech, morphology etc. for each word, named entity recognition etc.')

parser = reqparse.RequestParser()
parser.add_argument('sentence', required=True, help='The sentence which words will be deeply analyzed',location='args')

ner_model = api.model('NER', {
    'text' : fields.String(required=True, description='The current word as simple text'),
    'start' : fields.Integer(required=True, description='The current word position start within the sentence'),
    'end' : fields.Integer(required=True, description='The current word position end within the sentence'),
    'entity' : fields.String(required=True, description='The entity name')
})

class POSFormatter(fields.Raw):
    def format(self, value:POSTypeEnum):
        return value.value

class TextTypeFormatter(fields.Raw):
    def format(self, value:TextTypeEnum):
        return value.value

sentence_model = api.model('SentenceAnalysis', {
    'text' : fields.String(description='The text content of the token'),
    'language' : fields.String(description='The language of the token'),
    'start' : fields.Integer(description='The start position of the token'),
    'end' : fields.Integer(description='The end position of the token'),
    'start_sentence' : fields.Boolean(description='The token is the first word of the sentence?'),
    'end_sentence' : fields.Boolean(description='The token is the last word of the sentence?'),
    'pos' : POSFormatter(attribute='pos', description='The part of speech of the token'),
    'lemma' : fields.String(description='The part lemma of the token'),
    'corrected_text' : fields.String(description='The corrected token'),
    'stem' : fields.String(description='The part of speech of the token'),
    'morphological' : fields.Raw(description='The morphologic context for the token'), 
    'shape' : fields.String(description='The form of the token'),
    'text_type' : TextTypeFormatter(attribute='text_type', description='The supposed type of the token'),
    'is_stopword' : fields.Boolean(description='The current token is a stop word (it may not be encluded in text classification operation)'),
    'start' : fields.Integer(description='The current word position start within the sentence'),
    'end' : fields.Integer(description='The current word position end within the sentence')
})

output_model = api.model('SentenceFullAnalysis',{
    'sentence_analysis' : fields.List(fields.Nested(sentence_model)),
    'ner' : fields.List(fields.Nested(ner_model))
})

@api.route('/analyze/<string:language>')
@api.param('language', description='The language of the sentence', enum=DeepAnalyzerLanguageEnum._member_names_)
class DeepAnalysisResource(Resource):
    @api.expect(parser)
    @api.marshal_with(output_model)    
    def get(self, language):
        handler = DeepAnalyzerHandler(DeepAnalyzerLanguageEnum[language])
        sentence = parser.parse_args()['sentence'] 
        out = handler.Handle(sentence)
        return out