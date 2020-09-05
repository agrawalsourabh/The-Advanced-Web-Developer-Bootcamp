from flask import Blueprint, render_template

chap50 = Blueprint('chap50', __name__)

@chap50.route('/holygraillayout')
def holygraillayout():
    return render_template('chapter50/holygraillayout.html')