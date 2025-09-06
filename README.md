# Anime-Recommendation

This is a simple yet powerful **Anime Recommender System** built using **Python**. It recommends similar anime based on the selected title using content-based filtering and a pre-computed similarity matrix.

---

## ✨ Features

- 🔍 **Content-Based Anime Recommendation**  
  Select an anime and get 5 similar anime suggestions based on synopsis, genres, themes, cast, and director.

- 🧠 **NLP-powered Similarity Engine**  
  Uses **TF-IDF** or **CountVectorizer** vectorization and **cosine similarity** on processed tags to generate recommendations.

---

## 📁 Datasets Used

The system uses anime data, including:

- `anime.csv`: Contains metadata like title, genres, themes, synopsis, score, and more.

---

## 🛠️ How It Works

1. **Data Cleaning & Preprocessing**
   - Handles missing values and removes duplicates.
   - Extracts top cast members and director information.
   - Cleans and normalizes text fields (removes spaces, converts to lowercase, stemming).

2. **Feature Engineering**
   - Combines synopsis, genres, themes, cast, and director into a single `tags` column.

3. **Vectorization & Similarity**
   - Uses **TF-IDF** or **CountVectorizer** to convert `tags` into numerical vectors.
   - Calculates **cosine similarity** to find and rank similar anime.

4. **Recommendation Function**
   - Given an anime title, returns top-N recommended anime sorted by similarity.

---

## 🧠 Tech Stack
1. Python  
2. Pandas  
3. Scikit-learn  
4. NLTK (for stemming)  
