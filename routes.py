from flask import Blueprint, request, jsonify
from models import Movie
from app import db

# Define the blueprint
api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/')
def index():
    return jsonify({"message": "Welcome to the Movie API! Refer to the documentation for available endpoints."}), 200


# Route to add a new movie
@api_blueprint.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    try:
        movie = Movie(
            title=data['title'],
            director=data.get('director'),
            genre=data.get('genre'),
            release_year=data.get('release_year'),
            rating=data.get('rating')
        )
        db.session.add(movie)
        db.session.commit()
        return jsonify({"message": "Movie added successfully", "movie_id": movie.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all movies
@api_blueprint.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.as_dict() for movie in movies]), 200

# Route to get a specific movie by ID
@api_blueprint.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return jsonify(movie.as_dict()), 200

# Route to update a movie
@api_blueprint.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    data = request.get_json()
    movie = Movie.query.get_or_404(movie_id)
    try:
        movie.title = data.get('title', movie.title)
        movie.director = data.get('director', movie.director)
        movie.genre = data.get('genre', movie.genre)
        movie.release_year = data.get('release_year', movie.release_year)
        movie.rating = data.get('rating', movie.rating)
        db.session.commit()
        return jsonify({"message": "Movie updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to delete a movie
@api_blueprint.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    try:
        db.session.delete(movie)
        db.session.commit()
        return jsonify({"message": "Movie deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
