#coding:utf8
from functools import wraps
from flask import redirect
from database import User

#自定义模板过滤器
from flask import session, current_app, g


def do_index_filter(index):
    if index == 1:
        return "first"
    elif index == 2:
        return "second"
    elif index == 3:
        return "third"
    else:
        return ""


#装饰器,封装用户登陆数据
#判断用户是否登录，如果登录了，把登录信息放到g
#一般定义装饰器的话可以不用加wrapper,但是如果多个函数被两个装饰器装饰时就报错,因为两个函数名一样,第二个函数再去装饰的话就报错
def user_islogin(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        user_id = session.get("user_id")
        if not user_id:
            return redirect("/")
        user = User.query.filter(User.id == user_id).first()
        g.user = user
        return func(*args,**kwargs)
    return wrapper
