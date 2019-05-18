from flask import session, g
import config
from .views import bp
from .models import CMSUser, CMSPermission

@bp.before_app_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user = user


@bp.context_processor
def cms_context_processor():
    return {"CMSPermission": CMSPermission}