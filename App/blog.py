# 关于模型，应该建哪几个，先分析，列一个软件的功能列表，完成这个功能需要数据库提供哪些数据
# 建完表之后，看看能不能完成基础功能，不行再改，先有数据再能交互
from datetime import datetime

from flask._compat import text_type
from flask_login import UserMixin

from App.ext import db, login_manager

'''
文章表
aid：主键  自增
title：标题
content：内容
create_time:发布时间
author：作者
category：类别
hits：点击量
comments：品论量
'''


class Article(db.Model):
    aid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=True)
    content = db.Column(db.String(1000))
    create_time = db.Column(db.DateTime, default=datetime.now)
    # uid=db.Column(db.Integer)  #可建可不建外键，因为是个人博客，只有个人可以发表
    cid = db.Column(db.Integer, db.ForeignKey('category.cid', ondelete='CASCADE'))
    hits = db.Column(db.Integer, default=0)
    comments = db.Column(db.Integer, default=0)
    picture = db.Column(db.String(300))  # 存的是图片路径(相对于static的)，修改完之后可以直接在数据库中用sql指令修改或者导
    tags = db.relationship('Tag', backref='article', lazy='dynamic')
    # full_content=db.Column(db.String(10000))
    __tablename__ = 'article'


'''
用户表 ---可以去看注册时需要哪些信息，再往上添加
uid:主键 自增
用户名
密码
电话
email
头像
注册时间
是否禁止登录

'''


class User(db.Model,UserMixin):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(11))
    email = db.Column(db.String(200))
    portrait = db.Column(db.String(300))  # 数据库存图太慢了,所以放个路径
    regtime = db.Column(db.DateTime)
    isforbid = db.Column(db.Boolean, default=False)

    __tablename__ = 'user'

    def get_id(self):
        try:
            return text_type(self.uid)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

@login_manager.user_loader
def get_user(uid):
    return User.query.get(uid)


'''
类别表
cid:主键 自增
名称
文章数量
'''


class Category(db.Model):
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    num = db.Column(db.Integer, default=0)
    articles = db.relationship('Article', backref='category', lazy='dynamic')
    __tablename__ = 'category'


'''
标签表
tid:主键  自增
名称
文章id：外键  ---一篇文章有多个标签，弄成一对多就行
'''


class Tag(db.Model):
    tid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    aid = db.Column(db.Integer, db.ForeignKey('article.aid'))
    __tablename__ = 'tag'


'''
评论表
id：主键 自增
content：内容
create_time:时间
user：外键   关联用户
'''


class Mark(db.Model):
    mid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(1000))
    marker_name = db.Column(db.String(20))
    marker_portrait = db.Column(db.String(200))
    create_time = db.Column(db.DateTime)
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
    # aid=db.Column(db.Integer,db.ForeignKey('article.aid'))
    __tablename__ = 'mark'
