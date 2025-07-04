# 🎬 Movie Recommender System

This is a simple yet effective movie recommendation system built with Streamlit. It allows users to get personalized movie recommendations based on their favorite films and discover new ones.

---

## ✨ Features

* **Fuzzy Matching Search:** Don't remember the exact movie title? No problem! The system uses fuzzy matching to find the closest movie in its database.
* **Top 4 Recommendations:** Get a list of the top 4 similar movie recommendations based on your input.
* **IMDb Integration:** Easily search for more details about recommended movies on IMDb with a single click.
* **Rating Distribution Chart:** Visualize the rating distribution for your selected movie.
* **"Surprise Me!" Feature:** Discover highly-rated movies from the database at random for those times you can't decide what to watch.
* **User-Friendly Interface:** Built with Streamlit for an interactive and intuitive user experience.

---

## 🚀 How to Run Locally

To get this project up and running on your local machine, follow these steps:

### Prerequisites

* Python 3.7+
* `pip` (Python package installer)

### Installation

1.  **Clone the repository (or download the files):**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```
    (Replace `<your-repository-url>` and `<your-repository-directory>` with your actual repository information.)

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required libraries:**
    ```bash
    pip install streamlit pandas
    ```
    *(Note: Fuzzy matching is done using Python’s `difflib` which is part of the standard library.)*

5.  **Place your datasets:**
    Make sure you have the following CSV files in the same directory as your Streamlit application:
    * `dataset.csv`
    * `movieIdTitles.csv`
    * `MovieRecommendations.csv`

6.  **Run the Streamlit application:**
    ```bash
    streamlit run your_app_name.py
    ```
    (Replace `your_app_name.py` with the actual name of your Streamlit script, likely `app.py` or similar.)

    Your web browser should automatically open to the Streamlit application. If not, open your browser and go to `http://localhost:8501`.

---

## 📖 How to Use the App

1.  **Enter a Movie Title:** In the "Enter a movie title" text box, type the full name of your favorite movie (e.g., `Toy Story (1995)`). The system uses fuzzy matching, but accurate names lead to better results.
2.  **Get Recommendations:** Click the "🎯 Recommend Movies" button to see the top 4 similar movie recommendations.
3.  **Explore on IMDb:** Click the "🔗 IMDb Search" link next to each recommendation to find more details on IMDb.
4.  **Rating Distribution:** Below the recommendations, you'll see a bar chart showing the rating distribution for the movie you entered.
5.  **Surprise Me!:** Can't think of a movie? Click the "🎲 Surprise Me!" button to get a random highly-rated movie suggestion.

---



