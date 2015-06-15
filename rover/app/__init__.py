from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
app.config.from_object('config')

cors = CORS(app)
import views
from app import api
from models.connect_to_cluster import Conn

Conn()
