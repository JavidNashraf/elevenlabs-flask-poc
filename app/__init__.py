from dotenv import load_dotenv
from flask import Flask

def create_app():
    app = Flask(__name__)

    load_dotenv()

    with app.app_context():
        from .routes import main

    app.register_blueprint(main)

    return app
