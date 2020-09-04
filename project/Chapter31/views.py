from flask import Blueprint, render_template

chap31 = Blueprint('chap31', __name__)

@chap31.route('/loadingicon')
def loadingicon():
    return render_template('chapter31/loadingicon.html')