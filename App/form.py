import re

from flask import session
from flask_wtf import FlaskForm
from wtforms import IntegerField, ValidationError, StringField, PasswordField, BooleanField
from wtforms.validators import length, regexp, EqualTo, DataRequired

from App.blog import *


def check_phone(form1, field):
    if not re.match(r'1[35678]\d{9}$', field.data):
        raise ValidationError('电话号码不符合规则')


def check_password(form1, field):
    if not re.match(r'(?![A-Z]+$)(?![a-z]+$)(?!\d+$)(?![\W_]+$)\S{8,20}$', field.data):
        raise ValidationError('密码必须为8-20位，且为数字、字母或符号两种以上组成')


class RegisterForm(FlaskForm):
    phone = StringField('手机号', validators=[check_phone])
    # password=StringField('密码',validators=[regexp(re.match(r'(?![A-Z]+$)(?![a-z]+$)(?!\d+$)(?![\W_]+$)\S{8,20}$','password'),message='密码必须为8-20位，且为数字、字母或符号两种以上组成')])
    password = StringField('密码', validators=[check_password])
    confirm = PasswordField('确认密码', validators=[EqualTo('password', message='两次密码不一致，请重新输入')])
    username = StringField('用户名', validators=[DataRequired('请输入用户名')])
    code=StringField()
    sms = StringField()
    check=BooleanField('选择框',validators=[DataRequired('请先同意注册协议哦')])

    def validate_username(self, field):
        user = User.query.filter(User.username == field.data).first()
        if user:
            raise ValidationError('用户名重名，请重新输入')
        return field

    def validate_phone(self, field):
        user = User.query.filter(User.phone == field.data).first()
        if user:
            raise ValidationError('手机号重复，请重新输入')
        return field

    def validate_code(self,field):
        if field.data!=session.get('code'):
            raise ValidationError('验证码错误')

    def validate_sms(self,field):
        print(field.data,session.get('sms'))
        if field.data != session.get('sms'):
            raise ValidationError('短信验证失败')
