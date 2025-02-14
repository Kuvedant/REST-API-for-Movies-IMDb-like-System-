# REST-API-for-Movies-IMDb-like-System-

# Movie API: RESTful API for Movie Management

This project is a RESTful API for managing a movie database similar to IMDb. It allows users to perform CRUD (Create, Read, Update, Delete) operations on movies. The backend is built using **Flask** and **SQLite**, and the API communicates through JSON.

---

## **Features**

- Add a new movie to the database.
- Retrieve all movies or a specific movie by ID.
- Update movie details (title, director, genre, release year, and rating).
- Delete a movie from the database.

---

## **Getting Started**

### **Prerequisites**

1. **Python 3.8+**
   Ensure you have Python installed. Check the version using:
   ```bash
   python --version
    ```
2. **Install Required Libraries**
    - Flask
    - SQLAlchemy
    - Flask-RESTful

    *Install them using pip:*
   ```bash 
   pip install flask flask_sqlalchemy flask-restful
   ```
## **Project Structure**
```bash
movie_api/
│
├── app.py          # Main application file (entry point)
├── models.py       # Database model definitions
├── routes.py       # API routes (CRUD operations)
├── movies.db       # SQLite database (auto-generated)
├── requirements.txt # List of dependencies
└── README.md       # Documentation
```
## **Setup Instructions**
1. **Clone the Repository**
*Clone the project to your local machine:*

```bash
git clone <repository-url>
cd movie_api
```

2. **Install Dependencies**
*Install all required dependencies:*

```bash
pip install -r requirements.txt
```

3. **Initialize the Database**
*Create the database and table structure by running:*

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

4. **Run the Application**
Start the Flask server:

```bash
python app.py
```

*The API will be available at http://127.0.0.1:5000.*

