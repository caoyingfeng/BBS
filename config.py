import os

# SECRET_KEY = os.urandom(24)
# for test
SECRET_KEY = "abd"


TEMPLATES_AUTO_RELOAD = True
DEBUG = True

DB_USERNAME = 'root'
DB_PASSWORD = '199232cyl'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'bbs3'

# PERMANENT_SESSION_LIFETIME =

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False


CMS_USER_ID = "FEIA"
FRONT_USER_ID = "DSFEFE"

# MAIL_USE_TLS：端口号587
# MAIL_USE_SSL：端口号465
# QQ邮箱不支持非加密方式发送邮件
# 发送者邮箱的服务器地址
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL
MAIL_USERNAME = "164972038@qq.com"
MAIL_PASSWORD = "ymcqkpetudwcbihd"
MAIL_DEFAULT_SENDER = "164972038@qq.com"

# 阿里大于相关配置
# ALIDAYU_APP_KEY = 'LTAI7PMyzIRAqJ6z'
ALIDAYU_APP_SECRET = 'Dh7LLtF9s8WAzXnQeGHiVNf1AolpnD'


AccessKey_ID = 'LTAI7PMyzIRAqJ6z'
Access_Key_Secret ='Dh7LLtF9s8WAzXnQeGHiVNf1AolpnD'

ALIDAYU_SIGN_NAME = 'python论坛注册'
ALIDAYU_TEMPLATE_CODE = 'SMS_165414707'

# UEditor的相关配置

UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')

UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = "9FveJ45zc6Iwe1Oq_-uQnHTiUVHpCvQnFLVAw-9Q"
UEDITOR_QINIU_SECRET_KEY = "AaWhtWonHQ66ZLsGNPZM5FI2zm_JdCVSCN_mjdYp"
UEDITOR_QINIU_BUCKET_NAME = "cypython"
UEDITOR_QINIU_DOMAIN = "http://ps5uum1s1.bkt.clouddn.com"

# flask-paginate的相关配置
PER_PAGE = 10