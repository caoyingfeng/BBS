from ..forms import BaseForm
from wtforms import StringField
from wtforms.validators import Regexp

# class SignupForm(BaseForm):
#     telephone = StringField(validators=[Regexp(r'1[345789]\d{9}',message='请输入正确格式的手机号码！')])
#