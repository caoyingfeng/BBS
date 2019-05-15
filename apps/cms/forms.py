from wtforms import Form,StringField,IntegerField
from wtforms.validators import Email,Length,InputRequired,EqualTo
from ..forms import BaseForm


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确的邮箱地址'),
                                    InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(6,20,message='密码格式不正确')])
    remember = IntegerField()


class ResetpwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(6,20,message="请输入正确格式的旧密码")])
    newpwd = StringField(validators=[Length(6, 20, message="请输入正确格式的新密码")])
    newpwd2 = StringField(validators=[EqualTo("newpwd",message="两次密码不一致")])