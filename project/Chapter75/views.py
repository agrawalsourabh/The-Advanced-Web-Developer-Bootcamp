from flask import Blueprint, render_template

chap75 = Blueprint('chap75', __name__)

@chap75.route('/firstRequest')
def firstRequest():
    return render_template('chapter75/firstRequest.html')