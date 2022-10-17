from flask_restx import Resource, fields, Namespace, reqparse

from enums.spacy import SpacyLanguageEnum
from models.lemmatizer import LemmatizerModel
from handlers.lemmatizer import SpacyLemmatizerHandler

api = Namespace('lemmatizer', description='Lemmatize sentences words')

parser = reqparse.RequestParser()
parser.add_argument('sentences', required=True, action='append', location='args', help='A list of sentences which words will be lemmatized')

output_model = api.model('LemmatizedSentences', {
    'sentences' : fields.List(fields.String(), required=True, default=["sentence with lemmas1", "sentence with lemmas2"], description='A list of sentences which words have been lemmatized')
})

@api.param('language', 'The language of the sentences)', enum = SpacyLanguageEnum._member_names_)
class LemmatizerSpacyResource(Resource):
    @api.expect(parser)
    @api.marshal_with(output_model)
    def get(self, language):
        sentences = parser.parse_args()['sentences']

        lemmatizer = SpacyLemmatizerHandler(SpacyLanguageEnum[language])

        out = LemmatizerModel()
        for sentence in sentences:
           out.sentences.append(lemmatizer.LemmatizeSentence(sentence))

        return out

api.add_resource(LemmatizerSpacyResource, '/lemmatize/spacy/<string:language>')