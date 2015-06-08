from app import app
from flask import render_template
from models.sitter_profile import SitterProfile


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return(render_template('index.html'))


@app.route('/sitters', methods=['GET'])
def sitters():
    return(render_template('sitters.html',
                           sitters=SitterProfile.objects.all()))
