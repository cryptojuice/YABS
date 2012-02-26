from flask import Flask
from blog import settings
from views import  main
from views.main import main

app = Flask("blog")
app.register_blueprint(main)
app.config['SECRET_KEY'] = settings.SECRET_KEY
app.wsgi_app = ProxyFix(app.wsgi_app)

