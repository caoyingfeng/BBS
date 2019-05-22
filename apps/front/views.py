from flask import (
    Blueprint,
    views,
    render_template,
    request
)
from .forms import SignupForm
from utils import restful
from .models import FrontUser
from exts import db

bp = Blueprint('front',__name__)


@bp.route('/')
def index():
    return 'front index'

class SignupView(views.MethodView):
    def get(self):
        return render_template("front/front_signup.html")
    def post(self):
        form = SignupForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            username = form.telephone.data
            password = form.password1.data
            user = FrontUser(telephone=telephone,username=username,password=password)
            db.session.add(user)
            db.session.commit()
            return restful.success()
        else:
            print(form.get_error())
            return restful.param_error(message=form.get_error())


bp.add_url_rule('/signup/',view_func=SignupView.as_view('signup'))