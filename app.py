from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import routes to register API endpoints
from routes import api_blueprint
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    # Run the server
    app.run(debug=True)
