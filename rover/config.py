import os
import jinja2

from flask_restful import Api
from app import app

basedir = os.path.abspath(os.path.dirname(__file__))
script_dir = os.path.dirname(__file__)

CSRF_ENABLED = True
SECRET_KEY = 'Replace_With_SecretKey'
# TODO<Ryan>: Change this to a command line argument
cassandra_cluster_ip = '127.0.0.1'
cassandra_default_keyspace = 'rover'

"""
The following alters the location that
Jinja2 looks for templates by default
"""
template_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader(['templates'])
    ])
app.jinja_loader = template_loader

api = Api(app)
