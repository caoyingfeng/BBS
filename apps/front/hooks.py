import config
from flask import session,g
from .models import FrontUser
from .views import bp


@bp.before_app_request
def before_request():
    if config.FRONT_USER_ID in session:
        user_id = session.get(config.FRONT_USER_ID)
        user = FrontUser.query.get(user_id)
        if user:
            g.front_user = user


