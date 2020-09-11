from flask import Blueprint, render_template

chap81 = Blueprint('chap81', __name__)

@chap81.route("/fetcherrorhandling")
def fetcherrorhandling():
    return render_template('chapter81/fetcherrorhandling.html')