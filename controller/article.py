from flask import render_template, Blueprint

# 导入model
from model.article_model import Article


article = Blueprint('article', __name__)


@article.route('')
def show():
    return render_template('article.html')
