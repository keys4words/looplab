from flask import Flask

app = Flask(__name__)

from .views import *
from .profiles.views import *
from .jobs.views import *

# flask run --reload --debugger