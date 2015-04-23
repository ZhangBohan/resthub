from flask import Flask
from flask.ext.script import Manager
from redis import StrictRedis

from .qrcodes import qrcodes as qrcodes_blueprint

app = Flask(__name__)

manager = Manager(app=app)

app.register_blueprint(qrcodes_blueprint, url_prefix='/qrcodes')


redis = StrictRedis()

@app.route('/')
def hello_world():
    return 'Hello World!'