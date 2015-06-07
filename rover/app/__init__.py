from flask import Flask

app = Flask(__name__)

from app import app
from utils.data.scheduled_processes import Scheduler

#  Run schduled processes on a loop
Scheduler()
