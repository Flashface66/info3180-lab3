from flask import Flask
from flask_mail import Mail
from .config import Config
from flask_wtf.csrf import CSRFProtect
from app.forms import ContactForm


app = Flask(__name__)
app.config.from_object(Config)


csrf = CSRFProtect(app)
csrf.init_app(app)
mail = Mail(app)
from app import views