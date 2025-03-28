# Attributes:
#     name
#     year
#     rating
    
#     Methods:
#         pause
#         play
#         forward




import math
class Movie:
    def __init__(self,name,year,rating):
        self.name = name
        self.year = year
        self.rating = rating
    def name_print(movie):
        print("Name of the movie is: " + movie.name)
    def play(movie):
        print("playing movie: " + movie.name)
    def pause(movie):
        print("pause the movie: " + movie.name)
        
    def compare(movie1,movie2):
        if movie1.rating > movie2.rating :  
            print("this movie has the highest rating: "+ movie1.rating)
        else:
            print("this movie has higher raitng: "+ movie2.rating )
    pass
    # name = "Andaz Apna Apna"
    
Movie1 = Movie("3Idiots",2009,4.9)
# Movie2 = Movie()
Movie.name_print(Movie1)
Movie1.name_print()

Movie2 = Movie("Taare Zameen Par",2007,4.9)
Movie.compare(Movie1,Movie2)
Movie1.compare(Movie2)    #2nd alternative to use the upper compare method
Movie2.compare(Movie1)    #3rd alternative to use the upper compare method

