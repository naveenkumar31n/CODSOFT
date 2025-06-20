import pandas as pd

df = pd.read_csv("TamilMovies.csv")

def recommend_movies_by_genre(genre):
    matches = df[df['genre'].str.lower() == genre.lower()]
    
    if matches.empty:
        print(" No movies found in this genre.")
    else:
        print(f"\n🎬 Recommended Tamil {genre} Movies:\n")
        for _, row in matches.iterrows():
            print(f" {row['title']} ({row['year']}) - IMDb: {row['rating']}")

print("🎥 Tamil Movie Recommender")
user_genre = input("Enter a genre (Action/Romance/Drama/Thriller): ")

recommend_movies_by_genre(user_genre)
