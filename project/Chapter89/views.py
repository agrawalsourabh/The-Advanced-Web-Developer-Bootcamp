from flask import Blueprint, render_template

chap89 = Blueprint('chap89', __name__)

@chap89.route('/randomcatimgs')
def randomcatimgs():
    return render_template('chapter89/randomcatimgs.html')