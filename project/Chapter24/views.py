from flask import Blueprint, render_template

chap24 = Blueprint("chap24", __name__)

@chap24.route('/animated_gallery')
def animated_gallery():
    return render_template('chapter24/animated_gallery.html')