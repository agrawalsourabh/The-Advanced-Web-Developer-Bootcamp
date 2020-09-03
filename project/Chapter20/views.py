from flask import Blueprint, render_template

chap20 = Blueprint("chap20", __name__)

@chap20.route('/transition')
def transition():
    return render_template('chapter20/transition.html')