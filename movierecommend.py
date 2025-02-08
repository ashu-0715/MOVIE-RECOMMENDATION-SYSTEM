import pandas as pd

# Load the dataset
df = pd.read_csv('Tamil_movies_dataset.csv')

# Fill missing rating values with the average rating
df['Rating'].fillna(df['Rating'].mean(), inplace=True)

# Function to recommend movies based on a given movie name
def recommend_movies(movie_name):
    # Check if the movie is in the dataset
    if movie_name in df['MovieName'].values:
        print(f"Movies recommended based on '{movie_name}':\n")
        
        # Get the genre of the movie
        movie_genre = df[df['MovieName'] == movie_name]['Genre'].values[0]
        
        # Filter the movies based on the same genre
        recommendations = df[df['Genre'] == movie_genre]
        
        # Exclude the searched movie from recommendations
        recommendations = recommendations[recommendations['MovieName'] != movie_name]
        
        # Sort recommendations by rating (optional)
        recommendations = recommendations.sort_values(by='Rating', ascending=False)
        
        # Display top 5 recommendations with movie details
        for index, row in recommendations.head(10).iterrows():
            print(f"Movie: {row['MovieName']}")
            print(f"Genre: {row['Genre']}")
            print(f"Rating: {row['Rating']}")
            print(f"Director: {row['Director']}")
            print(f"Actor: {row['Actor']}")
            print(f"Year: {row['Year']}")
            print(f"Hero Rating: {row['Hero_Rating']}")
            print(f"Content Rating: {row['content_rating']}")
            print('-' * 50)
    else:
        print("Movie not found. Please check the name.")

# Taking user input for movie name
user_input = input("Enter the movie name: ")
recommend_movies(user_input)
