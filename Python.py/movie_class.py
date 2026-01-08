class Movie:
    def __init__(self, name, release_date, budget, collection, genre, director):
        self.name = name
        self.release_date = release_date
        self.budget = budget
        self.collection = collection
        self.genre = genre
        self.director = director

    def profit(self):
        return self.collection - self.budget

    def roi(self):
        if self.budget == 0:
            return 0
        return (self.profit() / self.budget) * 100

    def status(self):
        if self.roi() >= 100:
            return "BLOCKBUSTER HIT"
        elif self.roi() >= 50:
            return "HIT"
        elif self.roi() >= 0:
            return "AVERAGE"
        else:
            return "FLOP"
