
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = "d26209c3e5f21a113611c0111ea1a9bc"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
Bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from fakepinterest import routes