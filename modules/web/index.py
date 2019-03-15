# -*- encoding: utf-8 -*-
# from flask import Blueprint, render_template, session
# from database import User, Category, News
#
# index_blue = Blueprint('index_blue', import_name=__name__, template_folder='../../templates')
#
#
# @index_blue.route('/')
# def index():
#     data={}
#     user_id = session.get('user_id')
#     if user_id:
#         data['user_info'] = User.query.filter(User.id == user_id).first()
#     data['categoies'] = Category.query.all()
#     data['click_news_list'] = get_top10_news()
#
#     return render_template('./news/index.html', data=data)
#
#
# def get_top10_news():
#     click_new_list = News.query.filter(News.status==2).order_by(News.clicks.desc()).offset(0).limit(10)
#     print(click_new_list)
#     click_list = []
#     for new in click_new_list:
#         click_list.append(new.to_dict())
#     print(click_list)
#     return click_list
from flask import Blueprint


index_blue = Blueprint('index_blue', import_name=__name__, template_folder='../../templates')


@index_blue.route('/')
def index():
    return 'ok'

