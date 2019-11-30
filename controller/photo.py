from flask import render_template, Blueprint

# 导入model
from model.photo_model import Photo


photo = Blueprint('photo', __name__)


@photo.route('')
def show():
    return render_template('photo.html')
