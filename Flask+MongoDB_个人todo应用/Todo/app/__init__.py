from flask import Flask
from flask_mongoengine import MongoEngine
app = Flask(__name__)
import config
app.config.from_object(config)

db = MongoEngine(app)


from app import views,models