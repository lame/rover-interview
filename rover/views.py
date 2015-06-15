from app import app
from flask import render_template
from models.sitter_profile import SitterProfile
# from threading import Thread
# from utils.data.scheduled_processes import Scheduler


# Application hangs on process rather than continuing
# past is as a Daemon, not sure why
# @app.before_first_request
# def run_scheduled_process():
#     processes = []

#     t = Thread(target=Scheduler(), args=())
#     t.daemon = True
#     print('starting t')
#     t.start()
#     processes.append(t)

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return(render_template('index.html'))


@app.route('/sitters', methods=['GET'])
def sitters():
    return(render_template('sitters.html',
                           sitters=SitterProfile.objects.all().limit(10)))
