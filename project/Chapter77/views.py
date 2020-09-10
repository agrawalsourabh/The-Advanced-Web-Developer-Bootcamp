from flask import Blueprint, render_template

chap77 = Blueprint('chap77', __name__)

@chap77.route('/bitcoinprice')
def bitcoinprice():
    return render_template('chapter77/bitcoinprice.html')