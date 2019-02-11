from flask import Flask
from config import Config

app = Flask(__name__)
app.config.form_object(Config)

from 5pm-findtheroommate import routes
