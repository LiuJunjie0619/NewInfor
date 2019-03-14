# -*- encoding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
import config


app = Flask(__name__)
app.config.from_object(config.config_dict['config'])
db = SQLAlchemy(app)


# 父类
class Base(object):
    create_time = db.Column(db.DateTime, default=datetime.now())    # 数据创建时间
    update_time = db.Column(db.DateTime, default=datetime.now())    # 数据修改时间


# 新闻分类表
class Category(Base, db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    relate_news = db.relationship('News', backref='relate_category', lazy='dynamic')    # 分类下的新闻列表


# 管理员表
class Admin(Base, db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    pass_hash = db.Column(db.String(200), nullable=False)


# 用户收藏，多对多 关系表
table_user_news = db.Table('user_collection',
                           db.Column('id', db.Integer, primary_key=True),
                           db.Column('user_id', db.Integer, db.ForeignKey('user.id')),  # 用户Id
                           db.Column('news_id', db.Integer, db.ForeignKey('news.id')))  # 新闻Id


# 新闻表
class News(Base, db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))            # 新闻标题
    source = db.Column(db.String(30))           # 新闻来源
    index_image_u = db.Column(db.String(100))   # 新闻展示的缩略图路径
    digest = db.Column(db.String(255))          # 新闻摘要
    clicks = db.Column(db.Integer)              # 新闻被点击次数
    content = db.Column(db.Text)                # 新闻内容
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))   # 新闻分类Id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))           # 新闻发布人Id
    status = db.Column(db.Integer)              # 新闻状态 1审核中 2通过 3未通过
    reason = db.Column(db.String(100))          # 审核失败的原因

    def to_dict(self):
        new_dict = \
            {
                'id': self.id,
                'title':self.title,
                'source':self.source,
                'index_image_u':self.index_image_u,
                'digest': self.digest,
                'clicks': self.clicks,
                'content': self.content,
                'category_id': self.category_id,
                'user_id': self.user_id,
                'status': self.status,
                'reason': self.reason,
                'create_time': self.create_time.strftime('%Y-%m-%D %H:%M:%S')
            }
        return new_dict


# 用户表
class User(Base, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(20), index=True)                    # 昵称
    password_has = db.Column(db.String(200), nullable=False)
    mobile = db.Column(db.String(11), nullable=False)                   # 手机号
    avatar_url = db.Column(db.String(256))                              # 用户头像路径
    last_login = db.Column(db.DateTime, default=datetime.now())         # 最后登录时间
    signature = db.Column(db.String(512))                               # 用户签名
    gender = db.Column(db.String(10), default='Man', nullable=False)    # 性别
    news = db.relationship('News', backref='author', lazy='dynamic')    # 用户发布的新闻
    news_collection = db.relationship('News', secondary=table_user_news
                                      , backref='users', lazy='dynamic')  # 用户收藏的新闻


# 新闻评论表
class Comment(Base, db.Model):
    __tablename__='comment'
    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer, db.ForeignKey("news.id"))       # 新闻Id
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))       # 用户Id,即：谁发布的评论
    content = db.Column(db.String(255))                             # 新闻内容


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(port=7865)
