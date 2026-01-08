import csv
from movie_class import Movie
from analyzer import BoxOfficeAnalyzer

movies = []

with open("/Users/foggypants/Desktop/Python.py/moviedata.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        movie = Movie(
            row["name"],
            row["release_date"],
            int(row["budget"]),
            int(row["collection"]),
            row["genre"],
            row["director"]
        )
        movies.append(movie)

print("Total movies loaded:", len(movies))

analyzer = BoxOfficeAnalyzer(movies)
analyzer.analyze()
