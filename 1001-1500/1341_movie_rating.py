'''
Pandas Schema:
data = [[1, 'Avengers'], [2, 'Frozen 2'], [3, 'Joker']]
movies = pd.DataFrame(data, columns=['movie_id', 'title']).astype({'movie_id':'Int64', 'title':'object'})
data = [[1, 'Daniel'], [2, 'Monica'], [3, 'Maria'], [4, 'James']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})
data = [[1, 1, 3, '2020-01-12'], [1, 2, 4, '2020-02-11'], [1, 3, 2, '2020-02-12'], [1, 4, 1, '2020-01-01'], [2, 1, 5, '2020-02-17'], [2, 2, 2, '2020-02-01'], [2, 3, 2, '2020-03-01'], [3, 1, 3, '2020-02-22'], [3, 2, 4, '2020-02-25']]
movie_rating = pd.DataFrame(data, columns=['movie_id', 'user_id', 'rating', 'created_at']).astype({'movie_id':'Int64', 'user_id':'Int64', 'rating':'Int64', 'created_at':'datetime64[ns]'})
'''

import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    df = movies.merge(movie_rating, on='movie_id', how='right')
    df = df.merge(users, on='user_id', how='left')

    df1 = df.groupby('name')['user_id'].agg(count=('count')).reset_index()
    df1.sort_values(by=['count', 'name'], ascending=[False, True], inplace=True)
    person = df1.iloc[0]['name']

    df2 = df[(df['created_at'].dt.year == 2020) & (df['created_at'].dt.month == 2)]
    df2 = df2.groupby('title', as_index=True)['rating'].agg('mean').reset_index()
    df2.sort_values(by=['rating', 'title'], ascending=[False, True], inplace=True)
    movie = df2.iloc[0]['title']

    return pd.DataFrame({'results': [person, movie]})
