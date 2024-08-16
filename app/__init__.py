from flask import Flask
from .database import inti_app
from .routes import bp

def create_app():
    app = Flask(__name__)
    inti_app(app)
    app.register_blueprint(bp)

    return app
