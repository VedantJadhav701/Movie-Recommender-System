import streamlit as st
import pandas as pd
import difflib
import random

# Load datasets
ratings = pd.read_csv("dataset.csv", sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])
movies = pd.read_csv("movieIdTitles.csv")
recommendations_df = pd.read_csv("MovieRecommendations.csv")

# Merge ratings and movie titles
data = pd.merge(ratings, movies, on='item_id')
movie_stats = data.groupby('title').agg({'rating': ['mean', 'count']})
movie_stats.columns = ['AverageRating', 'RatingCount']
movie_stats = movie_stats.reset_index()

# App Title and Layout
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")
st.title("🎥 Movie Recommender System")
st.markdown("Type your favorite movie below and get 4 similar recommendations!")

# Display sample movies
st.subheader("🎞️ Sample Movie Titles")
st.markdown("Here's how your movie input should look:")

sample_movies = movies.sample(5).reset_index(drop=True)
st.table(sample_movies.rename(columns={'item_id': 'Movie ID', 'title': 'Movie Title'}))


# Sidebar Instructions
st.sidebar.title("📝 How to Use")
st.sidebar.markdown("""
1. Type the **full movie name** (e.g. *Toy Story (1995)*).
2. Get **top 4 similar movie** recommendations.
3. Use **🎲 Surprise Me!** to discover new picks.
4. Click [🔗 IMDb Search] to explore details.

ℹ️ Movie names are case-sensitive and must match titles in the database.
""")

# Search bar with fuzzy matching
movie_list = movies['title'].tolist()
user_input = st.text_input("Enter a movie title", "Toy Story (1995)")
similar_movies = difflib.get_close_matches(user_input, movie_list, n=1)
selected_movie = similar_movies[0] if similar_movies else None

if selected_movie:
    if st.button("🎯 Recommend Movies"):
        st.success(f"Top Recommendations for: {selected_movie}")
        result_row = recommendations_df[recommendations_df['title'] == selected_movie]
        if not result_row.empty:
            for i in range(1, 5):
                rec = result_row.iloc[0, i+2]  # Skipping first 3 cols
                st.markdown(f"**{i}. {rec}**")
                imdb_search = f"https://www.google.com/search?q={rec.replace(' ', '+')}+IMDb"
                st.markdown(f"[🔗 IMDb Search]({imdb_search})")
        else:
            st.warning("Sorry! No recommendations found.")
else:
    st.info("Enter a valid movie name.")


# Show rating chart of input movie
if selected_movie in movie_stats['title'].values:
    ratings_data = data[data['title'] == selected_movie]
    st.subheader("🎯 Rating Distribution")
    st.bar_chart(ratings_data['rating'].value_counts().sort_index())

# Surprise me feature
if st.button("🎲 Surprise Me!"):
    surprise = movie_stats.sort_values(by='AverageRating', ascending=False)
    surprise_movie = random.choice(surprise.head(100)['title'].tolist())
    st.info(f"Try Watching: {surprise_movie}")

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ by [Vedant Jadhav](https://www.linkedin.com/in/vedantjadhav701/) | AIML Student → ML Engineer '27"
)
