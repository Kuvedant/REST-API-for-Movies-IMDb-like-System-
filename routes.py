from flask import Blueprint, request, jsonify
from app import db
from models import Movie

# Create a Flask Blueprint
api_blueprint = Blueprint('api', __name__)

# Add a new movie
@api_blueprint.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    try:
        # Create a new movie
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

# Get all movies
@api_blueprint.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.as_dict() for movie in movies]), 200

# Get a specific movie by ID
@api_blueprint.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return jsonify(movie.as_dict()), 200

# Update an existing movie
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

# Delete a movie
@api_blueprint.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    try:
        db.session.delete(movie)
        db.session.commit()
        return jsonify({"message": "Movie deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
