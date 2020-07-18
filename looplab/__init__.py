from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig

app = Flask(__name__)
csrt = CSRFProtect(app)

app.config.from_object(DevelopmentConfig())

from .home.views import *
from .views import *
from .profiles.views import *
from .jobs.views import *

# flask run --reload --debugger
