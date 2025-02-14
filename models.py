from app import db

# Movie model
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=True)
    genre = db.Column(db.String(50), nullable=True)
    release_year = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Float, nullable=True)

    def as_dict(self):
        """Convert model instance to a dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "director": self.director,
            "genre": self.genre,
            "release_year": self.release_year,
            "rating": self.rating
        }
