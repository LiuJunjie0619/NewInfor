# -*- encoding: utf-8 -*-
from flask import Blueprint, session, render_template, redirect, url_for, request, flash, jsonify
from database import Admin, Category
import apps
# 用于生成密码和对比密码是否一致
from werkzeug.security import generate_password_hash, check_password_hash

admin_blue = Blueprint('admin_blue', import_name=__name__, template_folder='../../templates')


@admin_blue.route('/')
def index():
    user_id = session.get('a_user_id')
    if user_id:
        return render_template('/admin/index.html')
    else:
        return redirect(url_for('admin_blue.login'))


@admin_blue.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        if not all([user, pwd]):
            flash('信息不全')
        else:
            a = Admin.query.filter(Admin.name==user).first()
            if not a:
                flash('用户名不存在')
            else:
                if check_password_hash(a.pass_hash, pwd):
                    session['a_user_id'] = a.id
                    return redirect(url_for('admin_blue.index'))
                else:
                    flash('密码错误')
    return render_template('/admin/login.html')


@admin_blue.route('/add')
def add():
    pwd = generate_password_hash('123')
    a = Admin(name='ljj', pass_hash=pwd)
    apps.db.session.add(a)
    return 'ok'


@admin_blue.route('/newscate', methods=['GET', 'POST'])
def news_cate():
    if request.method == 'POST':

        msg = {}
        name = request.form.get('name')
        if name:
            c = Category(name=name)
            apps.db.session.add(c)
            msg['code'] = '200'
            msg['message'] = '添加成功'
        else:
            msg['code'] = '500'
            msg['message'] = '不能为空'
        return jsonify(msg)
    cate = Category.query.all()
    return render_template('/admin/news_type.html', category=cate)
