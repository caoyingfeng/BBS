from flask import session, g
import config
from .views import bp
from .models import CMSUser

@bp.before_app_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user = user