from flask import Blueprint, render_template

chap39 = Blueprint('chap39', __name__)

@chap39.route('/flexboxI')
def flexboxI():
    return render_template('chapter39/flexboxI.html')