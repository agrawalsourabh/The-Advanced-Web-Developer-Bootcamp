from flask import Blueprint, render_template

chap55 = Blueprint('chap55', __name__)

@chap55.route('/')
def index():
    return render_template('chapter55/proj_index.html')