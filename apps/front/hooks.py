import config
from flask import session,g,render_template
from .models import FrontUser
from .views import bp


@bp.before_app_request
def before_request():
    if config.FRONT_USER_ID in session:
        user_id = session.get(config.FRONT_USER_ID)
        user = FrontUser.query.get(user_id)
        if user:
            g.front_user = user


@bp.errorhandler
def page_not_found():
    return render_template('front/front_404.html')