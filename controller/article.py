from flask import render_template, Blueprint
article = Blueprint('article', __name__)


@article.route('')
def index():
    return render_template('article.html')
