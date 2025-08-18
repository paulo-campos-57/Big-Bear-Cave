import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask_cors import CORS
from db.db import db, DATABASE_URL
from routes.routes import bp as routes_bp
from models.models import *


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    CORS(app, origins=["http://localhost:5173"], supports_credentials=True)

    db.init_app(app)

    app.register_blueprint(routes_bp)

    with app.app_context():
        db.create_all()


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
