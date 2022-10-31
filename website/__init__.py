from flask import Flask
from config import FlaskConfiguration


app = Flask(__name__)
app.config.from_object(FlaskConfiguration)
