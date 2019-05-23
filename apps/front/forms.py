from ..forms import BaseForm
from wtforms import StringField
from wtforms.validators import Regexp,equal_to,ValidationError
from utils import mycache
from exts import db
from .models import FrontUser

class SignupForm(BaseForm):
    telephone = StringField(validators=[Regexp(r'1[345789]\d{9}',message='请输入正确格式的手机号码！')])
    sms_captcha = StringField(validators=[Regexp(r'\w{4}',message='请输入正确格式的验证码')])
    username = StringField(validators=[Regexp(r'.{2,20}',message='请输入正确格式的用户名')])
    password1 = StringField(validators=[Regexp(r'[0-9a-zA-Z_\.]{6,20}',message='请输入正确格式的密码')])
    password2 = StringField(validators=[equal_to("password1",message='两次密码不一致')])
    graph_captcha = StringField(validators=[Regexp(r'\w{4}', message='请输入正确格式的验证码')])

    def validate_telephone(self,filed):
        telephone = filed.data
        user = FrontUser.query.filter(FrontUser.telephone==telephone).first()
        db.session.commit()
        if user:
            raise ValidationError(message='该手机号已存在')


    def validate_sms_captcha(self,filed):
        sms_captcha = filed.data
        telephone = self.telephone.data

        sms_captcha_mem = mycache.get(telephone)
        if not sms_captcha_mem or sms_captcha_mem.lower() != sms_captcha.lower():
            raise ValidationError(message='短信验证码错误')

    def validate_graph_captcha(self,filed):
        graph_captcha = filed.data

        graph_captcha_mem = mycache.get(graph_captcha)
        if not graph_captcha_mem:
            raise ValidationError(message='图形验证码错误')
