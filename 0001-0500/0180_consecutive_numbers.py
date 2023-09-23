'''
Pandas Schema:
data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
logs = pd.DataFrame(data, columns=['id', 'num']).astype({'id':'Int64', 'num':'Int64'})
'''

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    consecutives = set()
    count = 1
    prev = None

    for idx, row in logs.iterrows():
        val = row['num']

        if prev is not None:
            if val == prev:
                count += 1
            else:
                if count >= 3:
                    consecutives.add(prev)
                count = 1
            
        prev = val

    if count >= 3:
        consecutives.add(prev)

    return pd.DataFrame({'ConsecutiveNums': list(consecutives)})
