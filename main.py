from recommend import recommend_movies

print("===== FUZZY MOVIE RECOMMENDATION SYSTEM =====")
n = int(input("How many movie recommendations do you want? "))

result = recommend_movies(n)

print("\nTop Recommended Movies:\n")
print(result[['title', 'genre', 'rating', 'popularity', 'score']])
