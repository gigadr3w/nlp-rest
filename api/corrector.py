from flask_restx import Namespace, Resource, fields
from enums.correctors import EnumCorrector

api = Namespace('corrector', description='Method that correct an entire statement due to the specified languages')

input_model = api.model('ToCorrect', {
    'statement' : fields.String(required=True, description='The statement that have to been corrected') 
})

output_model = api.model('Corrected', {
    'statement' : fields.String(description='The corrected statement') 
})

@api.route('/corrector/<string:language>')
@api.param('language', description='The language of the dictionary with which correct the statement', enum=EnumCorrector._member_names_)
class Corrector(Resource):
    @api.expect(input_model)
    @api.marshal_with(output_model)
    def post(self, language):
        key = EnumCorrector[language]
        result = dict()
        result['statement'] = api.payload['statement'] + ' corrected'
        return result