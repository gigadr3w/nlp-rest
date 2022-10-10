from flask_restx import Resource, fields, Namespace

from enums.spacy import SpacyLanguageEnum
from models.lemmatizer import LemmatizerModel
from handlers.spacy import SpacyHandler

api = Namespace('lemmatizer', description='Methods to lemmatize words within a sentence')

input_model = api.model('ToLemmatize', {
    'sentences' : fields.List(fields.String(), required=True, default=["sentence1", "sentence2"], description='A list of sentences which words will lemmatized')
})

output_model = api.model('Lemmatized', {
    'sentences' : fields.List(fields.String(), required=True, default=["sentence1 with lemmas", "sentence1 with lemmas"], description='A list of sentences which words have been lemmatized')
})

@api.param('language', 'The language of the spacy dictionary used to lemmatize words (it must equal to the sentences language)', enum = SpacyLanguageEnum._member_names_)
class LemmatizerSpacyResource(Resource):
    @api.expect(input_model)
    @api.marshal_with(output_model)
    def post(self, language):
        sentences = api.payload['sentences']

        lemmatizer = SpacyHandler(SpacyLanguageEnum[language])

        out = LemmatizerModel()
        for sentence in sentences:
           out.sentences.append(lemmatizer.LemmatizeSentence(sentence))

        return out

api.add_resource(LemmatizerSpacyResource, '/lemmatize/spacy/<string:language>')