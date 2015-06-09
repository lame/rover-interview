from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

#FIXME<Ryan>: Add CORS support for production
from app import api
from models.connect_to_cluster import Conn
from utils.data.scheduled_processes import Scheduler

Conn()
#  Run schduled processes on a loop
# Scheduler()
