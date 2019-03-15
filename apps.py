# -*- encoding: utf-8 -*-
from flask import Flask
import config
from modules.web.index import index_blue
from modules.web.user import user_blue
from modules.admin.admin import admin_blue
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


app = Flask(__name__)
app.config.from_object(config.config_dict['config'])

# 首页，新闻展示
app.register_blueprint(index_blue, url_prefix='/')
# 用户信息相关
app.register_blueprint(user_blue, url_prefix='/user')
# 管理员模块
app.register_blueprint(admin_blue, url_prefix='/admin')

db = SQLAlchemy(app)
CSRFProtect(app)
