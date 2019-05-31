from flask import (
    Blueprint,
    views,
    render_template,
    request,
    session,
    url_for,
    g
)
from .forms import SignupForm,SigninForm,AddPostForm
from utils import restful, safeutils
from .models import FrontUser
from exts import db
import config
from ..models import BannerModel,BoardModel, PostModel
from .decorators import login_required
from flask_paginate import Pagination, get_page_parameter


bp = Blueprint('front',__name__)


@bp.route('/')
def index():
    banners = BannerModel.query.order_by(BannerModel.priority.desc()).limit(4)
    boards = BoardModel.query.all()
    page = request.args.get(get_page_parameter(),type=int,default=1)
    start = (page-1)*config.PER_PAGE
    end = start + config.PER_PAGE
    posts = PostModel.query.slice(start,end)
    pagination = Pagination(page=page,total=PostModel.query.count())
    # 将键值对解析成关键字参数
    context = {
        "banners":banners,
        "boards":boards,
        "posts":posts,
        "pagination":pagination
    }
    return render_template('front/front_index.html',**context)


@bp.route('/apost/',methods=['POST','GET'])
@login_required
def apost():
    if request.method == 'GET':
        boards = BoardModel.query.all()
        return render_template('front/front_apost.html',boards=boards)
    else:
        form = AddPostForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            board_id = form.board_id.data
            board = BoardModel.query.get(board_id)
            if not board:
                return restful.param_error(message="没有这个板块")
            else:
                post = PostModel(title=title,content=content)
                post.board = board
                post.author = g.front_user
                db.session.add(post)
                db.session.commit()
                return restful.success()
        else:
            return restful.param_error(message=form.get_error())


class SignupView(views.MethodView):
    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and safeutils.is_safe_url(return_to):
            return render_template("front/front_signup.html",return_to=return_to)
        else:
            return render_template("front/front_signup.html")
    def post(self):
        form = SignupForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            username = form.username.data
            password = form.password1.data
            user = FrontUser(telephone=telephone,username=username,password=password)
            db.session.add(user)
            db.session.commit()
            return restful.success()
        else:
            # print(form.errors)
            # print(form.errors.popitem()) 注意测试的时候打印popitem一次了，return再次调用无直可以pop
            # print(form.get_error())
            return restful.param_error(message=form.get_error())


class SigninView(views.MethodView):

    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and return_to != url_for('front.signup') and safeutils.is_safe_url(return_to):
            return render_template('front/front_signin.html',return_to=return_to)
        else:
            return render_template('front/front_signin.html')

    def post(self):
        form = SigninForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            password = form.password.data
            remember = form.remember.data
            user = FrontUser.query.filter_by(telephone=telephone).first()
            if user and user.check_password(password):
                session[config.FRONT_USER_ID]=user.id
                if remember:
                    session.permanent = True
                return restful.success()
            else:
                return restful.param_error(message='手机号或密码错误')
        else:
            return restful.param_error(form.get_error())


bp.add_url_rule('/signup/',view_func=SignupView.as_view('signup'))
bp.add_url_rule('/signin/',view_func=SigninView.as_view('signin'))