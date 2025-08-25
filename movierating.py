# MOVIE rating program
class Movie:
    def __init__(self, title, director, year, genre, rating):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.rating = rating  # out of 10

    def display_info(self):
        print(f" Title: {self.title}")
        print(f" Director: {self.director}")
        print(f" Year: {self.year}")
        print(f" Genre: {self.genre}")
        print(f" Rating: {self.rating}/10")

    def update_rating(self, new_rating):
        if 0 <= new_rating <= 10:
            self.rating = new_rating
            print(f"Rating updated to {self.rating}/10")
        else:
            print("Invalid rating. Must be between 0 and 10.")

# Example usage
movie1 = Movie("The Shawshank Redemption", "Frank Darabont", 1994, "Drama", 9.3)
movie1.display_info()

movie1.update_rating(9.5)


