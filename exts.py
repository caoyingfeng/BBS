from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from utils.alidayu import AliyunAPI

db = SQLAlchemy()
mail = Mail()
alidayu = AliyunAPI()