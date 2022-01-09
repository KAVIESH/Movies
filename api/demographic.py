import pandas as pd
import numpy as np

df2 = pd.read_csv('final.csv')
c = df2['vote_average'].mean()
m = df2['vote_count'].quantile(0.9)

qmovies = df2.copy().loc[df2['vote_count']>=m]
def rating (x, m=m, C=c):
  v = x['vote_count']
  R = x['vote_average']
  return ((v/(v+m))*R)+((m/(v+m))*C)

qmovies['score'] = qmovies.apply(rating, axis = 1)
qmovies = qmovies.sort_values('score', ascending = False)
ouput = qmovies[['title_x', 'vote_count', 'vote_average', 'poster_link']].head(20).values.tolist()


