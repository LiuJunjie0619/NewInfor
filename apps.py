# -*- encoding: utf-8 -*-
from flask import Flask
import config
from modules.web.index import index_blue
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


app = Flask(__name__)
app.config.from_object(config.config_dict['config'])

app.register_blueprint(index_blue, url_prefix='')
db = SQLAlchemy(app)
CSRFProtect(app)
