'''
Pandas Schema:
data = [['0', '1'], ['1', '0'], ['2', '0'], ['2', '1']]
followers = pd.DataFrame(data, columns=['user_id', 'follower_id']).astype({'user_id':'Int64', 'follower_id':'Int64'})
'''

import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    counts = followers['user_id'].value_counts().reset_index().sort_values('user_id')
    counts.columns = ['user_id', 'followers_count']
    return pd.DataFrame(counts)
