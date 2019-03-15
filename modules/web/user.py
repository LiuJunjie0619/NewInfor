# -*- encoding: utf-8 -*-
from flask import Blueprint


user_blue = Blueprint('user_blue', import_name=__name__, template_folder='../../templates')


@user_blue.route('/')
def index():
    return 'ok'
