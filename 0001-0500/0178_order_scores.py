'''
Pandas Schema:
data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})
'''

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values(by='score', ascending=False, inplace=True)
    scores.drop(['id'], axis=1, inplace=True)

    rank = [1]
    prev = None

    for index, row in scores.iterrows():
        val = row['score']
        if prev != None: 
            rank.append(rank[-1] + 1 if val < prev else rank[-1])
        prev = val

    scores['rank'] = rank if len(scores) else []
    return scores
