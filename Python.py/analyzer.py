from collections import defaultdict

def logger(func):
    def wrapper(*args, **kwargs):
        print("\n--- Analysis Started ---\n")
        result = func(*args, **kwargs)
        print("\n--- Analysis Completed ---\n")
        return result
    return wrapper


class BoxOfficeAnalyzer:

    def __init__(self, movies):
        self.movies = movies

    @logger
    def analyze(self):
        self.basic_analysis()
        self.top_movies()
        self.genre_analysis()
        self.director_analysis()
        self.generate_report()

    def basic_analysis(self):
        print("MOVIE BOX-OFFICE ANALYSIS\n")

        for movie in self.movies:
            print(f"Movie: {movie.name}")
            print(f"Release Date: {movie.release_date}")
            print(f"Budget: {movie.budget}")
            print(f"Collection: {movie.collection}")
            print(f"Profit: {movie.profit()}")
            print(f"ROI: {round(movie.roi(), 2)}%")
            print(f"Status: {movie.status()}")
            print("-" * 30)

    def top_movies(self):
        top = sorted(self.movies, key=lambda m: m.collection, reverse=True)[:3]
        print("\nTOP GROSSING MOVIES:")
        for i, m in enumerate(top, start=1):
            print(f"{i}. {m.name} - {m.collection}")

    def genre_analysis(self):
        genre_data = defaultdict(list)

        for m in self.movies:
            genre_data[m.genre].append(m.collection)

        print("\nGENRE ANALYSIS:")
        for genre, values in genre_data.items():
            avg = sum(values) / len(values)
            print(f"{genre}: Average Collection = {round(avg, 2)}")

    def director_analysis(self):
        director_data = defaultdict(list)

        for m in self.movies:
            director_data[m.director].append(m)

        print("\nDIRECTOR ANALYSIS:")
        for director, movies in director_data.items():
            hits = sum(1 for m in movies if m.roi() >= 50)
            success_rate = (hits / len(movies)) * 100
            avg_collection = sum(m.collection for m in movies) / len(movies)

            print(f"Director: {director}")
            print(f"Total Movies: {len(movies)}")
            print(f"Average Collection: {round(avg_collection, 2)}")
            print(f"Success Rate: {round(success_rate, 2)}%")
            print("-" * 30)

    def generate_report(self):
        with open("financial_reports.txt", "w") as f:
            for m in self.movies:
                f.write(
                    f"{m.name} | Profit: {m.profit()} | ROI: {round(m.roi(),2)}% | Status: {m.status()}\n"
                )
