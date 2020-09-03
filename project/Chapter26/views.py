from flask import Blueprint, render_template

chap26 = Blueprint('chap26', __name__)

@chap26.route('/keyframes1')
def keyframes1():
    return render_template("chapter26/keyframes1.html")