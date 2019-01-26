import numpy as np  
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv('/Users/parthmaniar/Downloads/ml-latest-small/ratings.csv', sep=',', )
movie_titles = pd.read_csv('/Users/parthmaniar/Downloads/ml-latest-small/movies.csv')
df = pd.merge(df, movie_titles, on='movieId')
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['number_of_ratings'] = df.groupby('title')['rating'].count()

movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')
movie='Aladdin (1992)'
m1_user_rating = movie_matrix[movie]

similar_to_m1=movie_matrix.corrwith(m1_user_rating)

corr_m1 = pd.DataFrame(similar_to_m1, columns=['correlation'])
corr_m1.dropna(inplace=True)


corr_m1 = corr_m1.join(ratings['number_of_ratings'])
print(" Recommendations For %s are as follows : " % movie)
print(corr_m1[corr_m1['number_of_ratings'] > 50].sort_values(by='correlation', ascending=False).head(20))



#parthmaniar
