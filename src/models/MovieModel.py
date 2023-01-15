
from decouple import config
import pandas as pd
import random


class MovieModel():

    @classmethod
    def get_movie(self):
        #Obtener datos de la API
        df = pd.read_csv("src\models\movie_dataset.csv",delimiter=",")

        titles = df['title']
        genres = df['genres']
        avrg = df['vote_average']

        movies = {}


        for i in range(200):
            movies[i] = {'title':titles[i],'genres':genres[i],'rating':avrg[i]/2}

        movie = movies[random.randint(0,200)]
   
        
        return movie