from flask import Flask

app = Flask(__name__)


# Blueprints
from project.Chapter20.views import chap20
app.register_blueprint(chap20, url_prefix='/chap20')