import pandas as pd
from fuzzy_system import compute_recommendation

def recommend_movies(top_n=5):
    df = pd.read_csv("movies.csv")
    scores = []

    # Compute fuzzy score for each movie
    for i, row in df.iterrows():
        score = compute_recommendation(row['rating'], row['popularity'])
        scores.append(score)

    df['score'] = scores

    # Sort movies by fuzzy score, highest first
    df = df.sort_values(by='score', ascending=False)

    return df.head(top_n)
