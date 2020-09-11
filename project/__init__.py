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

from project.Chapter29.views import chap29
app.register_blueprint(chap29, url_prefix="/chap29")

from project.Chapter31.views import chap31
app.register_blueprint(chap31, url_prefix='/chap31')

from project.Chapter39.views import chap39
app.register_blueprint(chap39, url_prefix="/chap39")

from project.Chapter43.views import chap43
app.register_blueprint(chap43, url_prefix="/chap43")

from project.Chapter50.views import chap50
app.register_blueprint(chap50, url_prefix="/chap50")

from project.Chapter55.views import chap55
app.register_blueprint(chap55, url_prefix='/chap55')

from project.Chapter75.views import chap75
app.register_blueprint(chap75, url_prefix="/chap75")

from project.Chapter76.views  import chap76
app.register_blueprint(chap76, url_prefix='/chap76')

from project.Chapter77.views import chap77
app.register_blueprint(chap77, url_prefix="/chap77")

from project.Chapter79.views import chap79
app.register_blueprint(chap79, url_prefix="/chap79")

from project.Chapter81.views import chap81
app.register_blueprint(chap81, url_prefix='/chap81')

from project.Chapter82.views import chap82
app.register_blueprint(chap82, url_prefix="/chap82")