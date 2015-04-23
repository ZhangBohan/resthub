from . import api
from flask.ext.restful import Resource


class QRcodes(Resource):
    def get(self):
        return {'hello': 'Say "Hello, World!"'}


api.add_resource(QRcodes, '/')