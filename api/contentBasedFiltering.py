from sklearn.feature_extraction.text import countVerctorizer
from sklearn.metrics.pairwise import cosin_similarity
import pandas as pd
import numpy as np

df2 = pd.read_csv('final.csv')
df2 = df2[df2['soup'].notna()]
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2['soup'])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
df2 = df2.reset_index()
indices = pd.series(df2.index, index = df2['title_x'])
def getRecommendations(title, cosine_sim):
  idx = indices[title]
  sim_scores = list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
  sim_scores = sim_scores[1:11]
  movie_indices = [i[0] for i in sim_scores]
  return df2['title_x'].iloc[movie_indices]