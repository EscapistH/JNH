from flask import Blueprint, render_template, request, redirect, url_for
from .models import *

# error 视图部分
error = Blueprint('error', __name__)


# 捕获全局404错误，并引导跳转至其他页面
@error.app_errorhandler(404)
def handle_404(e):
    return render_template('error/404.html'), 404

# 捕获全局500错误，提示用户等待服务器恢复运行后访问
@error.app_errorhandler(500)
def handle_500(e):
    return render_template('error/500.html'), 500


# index视图部分
index = Blueprint('index', __name__)


@index.route('')
# 显示主页面，展示所有子页面
def show_index():
    return render_template('index/index.html')


# articles 视图部分
article = Blueprint('articles', __name__)


@article.route('')
# 查询所有article，返回给前端/articles页面展示
def show_all():
    articles = Article.query.order_by(Article.article_id.desc()).all()
    return render_template('articles/articles.html', articles=articles)


@article.route('/<int:article_id>')
# 通过article_id查询数据并返回给前端/articles/<article_id>页面展示
# 是/articles页面跳转至对应详细内容页的方式
def show_by_id(article_id):
    article_ = Article.query.get_or_404(article_id)
    return render_template('articles/content.html', article=article_)


@article.route('/<string:article_title>')
# 通过标题查询所有符合条件的article返回给前端/articles页面展示
def show_by_title(article_title):
    articles = Article.query.filter_by(article_title=article_title)
    return render_template('articles/articles.html', articles=articles)


@article.route('/add', methods=('POST', 'GET'))
# 添加一条article到数据库中
def add_one():
    from app import db
    if request.method == 'POST':
        article_ = Article(request.form['article_title'],
                           request.form['article_auth'],
                           request.form['article_content']
                           )
        db.session.add(article_)
        db.session.commit()
        return redirect(url_for('articles.show_all'))
    else:
        return render_template('articles/add.html')


# photos 视图部分
photo = Blueprint('photos', __name__)


@photo.route('')
def show_all():
    return render_template('photos/photos.html')
