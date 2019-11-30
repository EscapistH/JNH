from flask import Blueprint, render_template
from .models import *

# error 视图部分
error = Blueprint('error', __name__)


@error.app_errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404


@error.app_errorhandler(500)
def handle_500(e):
    return render_template('500.html'), 500


# index视图部分
index = Blueprint('index', __name__)


@index.route('')
def show():
    return render_template('index.html')


# article 视图部分
article = Blueprint('article', __name__)


@article.route('')
def show_all():
    articles = Article.query.all()
    return render_template('article.html')


# photo 视图部分
photo = Blueprint('photo', __name__)


@photo.route('')
def show_all():
    return render_template('photo.html')

