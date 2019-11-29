from flask import render_template, Blueprint


photo = Blueprint('photo', __name__)


@photo.route('')
def show():
    return render_template('photo.html')
