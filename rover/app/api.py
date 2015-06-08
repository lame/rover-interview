from config import api
from resources.sitter_resource import SittersAPI

api.add_resource(SittersAPI, '/api/sitters')
