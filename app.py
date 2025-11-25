import streamlit as st
import pandas as pd
from recommend import recommend_movies

st.set_page_config(page_title="Fuzzy Movie Recommendation", layout="centered")

# ---------- Custom CSS for Clean UI ----------
st.markdown("""
<style>
    .movie-card {
        padding: 15px;
        border-radius: 15px;
        background-color: #f8f9fa;
        border: 1px solid #e1e1e1;
        margin-bottom: 15px;
    }
    .title {
        font-size: 22px;
        font-weight: 700;
        color:black;
    }
    .subtitle {
        font-size: 16px;
        font-weight: 500;
        color: #555;
    }
    .score-box {
        background: #2ecc71;
        padding: 6px 15px;
        border-radius: 10px;
        color: white;
        font-weight: 600;
        float: right;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🎬 Fuzzy Movie Recommendation System")
st.write("Get personalized movie recommendations using fuzzy logic.")

# ---------- INPUT ----------
st.markdown("### 🔢 Number of recommendations you want:")
n = st.number_input("Select number", min_value=1, max_value=10, value=5)

# ---------- BUTTON ----------
if st.button("🎯 Recommend Movies"):
    df = recommend_movies(n)

    st.markdown("## ⭐ Top Recommended Movies")

    for _, row in df.iterrows():
        st.markdown(f"""
        <div class="movie-card">
            <div class="score-box">{row['score']:.2f}</div>
            <div class="title">{row['title']}</div>
            <div class="subtitle">{row['genre']} • Rating: {row['rating']} • Popularity: {row['popularity']}</div>
        </div>
        """, unsafe_allow_html=True)
