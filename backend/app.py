# app.py
from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

# Load pickled model and similarity matrix
anime_dict = pickle.load(open("anime_model.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

new_df = pd.DataFrame(anime_dict)
indices = pd.Series(new_df.index, index=new_df["title_final"]).drop_duplicates()

app = Flask(__name__)

def recommend_anime(title, top_n=5):
    if title not in indices:
        return []

    idx = indices[title]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]

    anime_indices = [i[0] for i in sim_scores]
    result = new_df.iloc[anime_indices][[
        "anime_id", "title_final", "score", "anime_url", "image_url"
    ]].to_dict(orient="records")

    return result

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    title = request.form.get("anime_title")
    recommendations = recommend_anime(title, top_n=5)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
