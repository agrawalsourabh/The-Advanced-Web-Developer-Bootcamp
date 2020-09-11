from flask import Blueprint, render_template

chap79 = Blueprint('chap79', __name__)

@chap79.route('/firstfetchreq')
def firstfetchreq():
    return render_template('chapter79/firstfetchreq.html')