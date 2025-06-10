'''
Pandas Schema:
data = [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})
'''

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    filtered = tweets[tweets['content'].apply(lambda x: len(x) > 15)]
    return filtered[['tweet_id']]
