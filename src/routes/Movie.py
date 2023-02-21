from flask import Blueprint, jsonify
from models.MovieModel import MovieModel
from firebase_admin import db
import requests
import random

main = Blueprint('movie_blueprint', __name__)


@main.route('/')
def get_movies():

    try:
        ref = db.reference('movie')
        movies_snapshot = ref.get()
        movies = [movie for movie in movies_snapshot.values()]     
        movies_send = random.sample(movies,9)
        return jsonify(movies_send), 200

    except Exception as e:
        return jsonify({'messagee': str(e)}), 404
        
@main.route('/movie')
def get_movie():

    try:
        ref = db.reference('movie')
        movies_snapshot = ref.get()
        movies = [movie for movie in movies_snapshot.values()]     
        random_movie = random.choice(movies)
        return jsonify(random_movie), 200

    except Exception as e:
        return jsonify({'messagee': str(e)}), 404


@main.route('/addrandom')
def add_movies():
    try:
        ref = db.reference('movie')
        api_key = "aeee0eff5cb9118b6d1cd7289a2ed3b1"
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&include_video=false&page=1&vote_count.gte=1000&vote_average.gte=7"

        response = requests.get(url)
        data = response.json()

        movies = data['results']
        selected_movies = random.sample(movies,20 )

        new_movie = []
        for movie in selected_movies:
            new_movie.append({
                "id":movie['id'],
                "title":movie['original_title'],
                "adult":movie['adult'],
                "vote_average":movie['vote_average'],
                "image_url":"https://image.tmdb.org/t/p/w1280" + movie['backdrop_path']
                })
        
        for movie in new_movie:
            ref.child(str(movie['id'])).set(movie)


        return jsonify(new_movie)

    except Exception as e:
        return jsonify({'messagee': str(e)}), 404


