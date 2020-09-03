from flask import Blueprint, render_template

chap29 = Blueprint('chap29', __name__)

@chap29.route('/raising_setting_sun')
def raising_setting_sun():
    return render_template('chapter29/raising_setting_sun.html')