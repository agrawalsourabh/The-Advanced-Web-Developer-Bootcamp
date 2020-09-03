from flask import Flask

app = Flask(__name__)


# Blueprints
from project.Chapter20.views import chap20
app.register_blueprint(chap20, url_prefix='/chap20')

from project.Chapter21.views import chap21
app.register_blueprint(chap21, url_prefix='/chap21')

from project.Chapter24.views import chap24
app.register_blueprint(chap24, url_prefix="/chap24")

from project.Chapter26.views import chap26
app.register_blueprint(chap26, url_prefix="/chap26")