from flask import Blueprint
from flask.ext.restful import Api

__author__ = 'bohan'

qrcodes = Blueprint('qrcodes', __name__)

api = Api(app=qrcodes)

from . import views
