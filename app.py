from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize database object (db will be linked later to the app)
db = SQLAlchemy()

def create_app():
    # Application factory
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database with the app
    db.init_app(app)

    # Register blueprints
    from routes import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
