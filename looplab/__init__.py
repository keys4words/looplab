from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import DevelopmentConfig

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config.from_object(DevelopmentConfig())
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from .home.views import *
from .views import *
from .profiles.views import *

# flask run --reload --debugger
