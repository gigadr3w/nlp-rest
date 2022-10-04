from flask_restx import Namespace, Resource

api = Namespace('about', description='About this app')

@api.route('/about')
class Test1(Resource):
    def get(self):
        return '...what I have to write about it? Enjoy :)'