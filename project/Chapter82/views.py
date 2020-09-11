from flask import Blueprint, render_template

chap82 = Blueprint('chap82', __name__)

@chap82.route("/randomuser")
def randomuser():
    return render_template('chapter82/randomuser.html')