
from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, login_required

# from App.model import *
from App.blog import *

us=Blueprint('us',__name__,url_prefix='/user')

@us.route('/login/',methods=['POST','GET'])
def user_login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        user=User.query.filter(User.username==username,User.password==password).first()
        print(user)
        if user:
            login_user(user)
            return redirect(url_for('blog.home'))
        # else:
        #     flash('用户名或密码错误')
    return render_template('login.htm')

@us.route('/logout/')
def user_logout():
    logout_user()
    return redirect('/user/login/')

# @us.route('/reply/')
# @login_required
# def reply_article():
#     return redirect('/user/login/')