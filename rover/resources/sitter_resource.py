from flask import jsonify
from flask.ext.restful import Resource
from models.sitter_profile import SitterProfile


class SittersAPI(Resource):

    def get(self):
        return([dict(row) for row in SitterProfile.objects.all()])
