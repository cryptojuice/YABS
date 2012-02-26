from flask import Flask
from blog import settings
from views.views import main
from werkzeug.contrib.fixers import ProxyFix

app = Flask("blog")
app.register_blueprint(main)
app.config['SECRET_KEY'] = settings.SECRET_KEY
app.wsgi_app = ProxyFix(app.wsgi_app)

