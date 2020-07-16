from flask import Flask

app = Flask(__name__)

from .views import *
from looplab.profiles.views import *
from looplab.jobs.views import *