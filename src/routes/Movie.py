from flask import Blueprint,jsonify
from models.MovieModel import MovieModel

main = Blueprint('movie_blueprint',__name__)

@main.route('/')
def get_movies():

    try:
        m = MovieModel.get_movie()
        return jsonify(m),200 
    except Exception as e:
        return jsonify({'messagee':str(e)}),404