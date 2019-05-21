from flask import Blueprint, request
from utils import restful
from utils.captcha import Captcha
from exts import alidayu
from .forms import SMSCaptchaForm

bp = Blueprint('common',__name__,url_prefix='/c')


# @bp.route("/sms_captcha/")
# def sms_captcha():
#     # telephone=xxx
#     telephone = request.args.get('telephone')
#     if not telephone:
#         return restful.param_error(message='请输入手机号码')
#
#     captcha = Captcha.gene_text(number=4)
#     message = alidayu.send_sms(telephone, code=captcha)
#     if message == True:
#         return restful.success()
#     else:
#         # return restful.param_error(message=message)
#         return restful.success()

@bp.route("/sms_captcha/",methods=['POST'])
def sms_captcha():
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)
        message = alidayu.send_sms(telephone, code=captcha)
        if message:
            return restful.success()
        else:
            # return restful.param_error(message=message)
            return restful.success()
    else:
        return restful.param_error(message='参数错误')