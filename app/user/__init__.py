from flask import Flask, Blueprint

user = Blueprint('user', __name__)

from . import routes
