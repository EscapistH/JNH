from flask import Blueprint, render_template, request, redirect, url_for
from .models import *

# error 视图部分
error = Blueprint('error', __name__)


@error.app_errorhandler(404)
def handle_404(e):
    return render_template('error/404.html'), 404


@error.app_errorhandler(500)
def handle_500(e):
    return render_template('error/500.html'), 500


# index视图部分
index = Blueprint('index', __name__)


@index.route('')
def show_index():
    return render_template('index/index.html')


# articles 视图部分
article = Blueprint('articles', __name__)


@article.route('')
def show_all():
    articles = Article.query.all()
    return render_template('articles/articles.html', articles=articles)


@article.route('/<int:article_id>')
def show_by_id(article_id):
    article_ = Article.query.get_or_404(article_id)
    return render_template('articles/content.html', article=article_)


@article.route('/<string:article_title>')
def show_by_title(article_title):
    article_ = Article.query.filter_by(article_title=article_title).first_or_404()
    return render_template('articles/content.html', article=article_)


@article.route('/add', methods=('POST', 'GET'))
def add_one():
    from app import db
    if request.method == 'POST':
        article_ = Article(request.form['article_title'],
                           request.form['article_auth'],
                           request.form['article_content']
                           )
        db.session.add(article_)
        db.session.commit()
        return render_template(url_for('articles.show_by_id', article_id=request.form['article_id']))
    else:
        return render_template('articles/add.html')


# photos 视图部分
photo = Blueprint('photos', __name__)


@photo.route('')
def show_all():
    return render_template('photos/photos.html')
