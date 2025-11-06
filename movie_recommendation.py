# CODSOFT Internship - Task 3
# Project: Movie Recommendation System

# Sample movie dataset with genres, rating, and year
movies = {
    "Inception": {"genres": ["sci-fi", "thriller", "action"], "rating": 8.8, "year": 2010},
    "Titanic": {"genres": ["romance", "drama"], "rating": 7.9, "year": 1997},
    "Avengers": {"genres": ["action", "sci-fi", "adventure"], "rating": 8.0, "year": 2012},
    "The Notebook": {"genres": ["romance", "drama"], "rating": 7.8, "year": 2004},
    "Interstellar": {"genres": ["sci-fi", "adventure", "drama"], "rating": 8.6, "year": 2014},
    "Joker": {"genres": ["drama", "thriller"], "rating": 8.4, "year": 2019},
    "Frozen": {"genres": ["animation", "family", "fantasy"], "rating": 7.4, "year": 2013},
    "The Dark Knight": {"genres": ["action", "thriller"], "rating": 9.0, "year": 2008},
    "Coco": {"genres": ["animation", "family", "music"], "rating": 8.4, "year": 2017},
    "Toy Story": {"genres": ["animation", "family", "comedy"], "rating": 8.3, "year": 1995},
    "Avatar": {"genres": ["sci-fi", "action", "adventure"], "rating": 7.8, "year": 2009},
    "La La Land": {"genres": ["romance", "music", "drama"], "rating": 8.0, "year": 2016},
    "Spider-Man: No Way Home": {"genres": ["action", "sci-fi", "adventure"], "rating": 8.3, "year": 2021},
    "Inside Out": {"genres": ["animation", "family", "fantasy"], "rating": 8.1, "year": 2015},
    "Up": {"genres": ["animation", "adventure", "family"], "rating": 8.2, "year": 2009}
}

def recommend_by_genre(genre):
    rec = [(m, d["rating"], d["year"]) for m, d in movies.items() if genre in d["genres"]]
    rec.sort(key=lambda x: x[1], reverse=True)
    return rec

def recommend_by_rating(min_rating):
    rec = [(m, d["rating"], d["year"]) for m, d in movies.items() if d["rating"] >= min_rating]
    rec.sort(key=lambda x: x[1], reverse=True)
    return rec

def show_recommendations(recommendations):
    if not recommendations:
        print("❌ No matching movies found. Try another option!\n")
    else:
        print("\n🎞️ Recommended Movies:\n")
        for movie, rating, year in recommendations:
            print(f"{movie} ({year})  ⭐ {rating}/10")
        print("\nEnjoy your movie! 🍿\n")

print("🎥 Welcome to the Advanced Movie Recommendation System 🎬\n")
print("You can get movie suggestions based on:")
print("1️⃣ Genre")
print("2️⃣ Minimum Rating\n")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    print("\nAvailable genres: action, sci-fi, drama, romance, thriller, animation, adventure, family, comedy, fantasy, music\n")
    user_genre = input("Enter your favorite genre: ").lower()
    results = recommend_by_genre(user_genre)
    show_recommendations(results)

elif choice == "2":
    min_rating = float(input("Enter minimum rating (e.g., 8.0): "))
    results = recommend_by_rating(min_rating)
    show_recommendations(results)

else:
    print("❌ Invalid choice. Please restart and select a valid option.")

print("Would you like another recommendation? (yes/no)")
again = input("> ").lower()

if again == "yes":
    print("\nRestart the program and try another option!")
else:
    print("\nThanks for using the Movie Recommendation System 😊")