from wtforms import Form,StringField,IntegerField
from wtforms.validators import Email,Length,InputRequired


class LoginForm(Form):
    email = StringField(validators=[Email(message='请输入正确的邮箱地址'),
                                    InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(6,20,message='密码格式不正确')])
    remember = IntegerField()