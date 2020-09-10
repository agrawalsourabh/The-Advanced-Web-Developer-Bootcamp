from flask import Blueprint, render_template

chap76 = Blueprint("chap76", __name__)

@chap76.route("/randomDogImage")
def randomDogImage():
    return render_template('chapter76/randomDogImage.html')