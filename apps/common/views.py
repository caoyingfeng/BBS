from flask import Blueprint, request,make_response,jsonify
from utils import restful
from utils.captcha import Captcha
from exts import alidayu
from .forms import SMSCaptchaForm
from io import BytesIO
from utils import mycache
import qiniu


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
            mycache.set(telephone,captcha)
            # 测试用
            print(captcha)
            return restful.success()
        else:
            # return restful.param_error(message=message)
            # 测试用
            mycache.set(telephone, captcha)
            return restful.success()
    else:
        return restful.param_error(message='参数错误')


@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    mycache.set(text.lower(),text.lower())
    out = BytesIO()
    image.save(out,'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = "image/png"
    return resp


@bp.route('/uptoken/')
def uptoken():
    access_key = 'M4zCEW4f9XPanbMN-Lb9O0S8j893f0e1ezAohFVL'
    secret_key = '7BKV7HeEKM3NDJk8_l_C89JI3SMmeUlAIatzl9d4'
    q = qiniu.Auth(access_key, secret_key)

    bucket = 'hyvideo'
    token = q.upload_token(bucket)
    return jsonify({'uptoken': token})