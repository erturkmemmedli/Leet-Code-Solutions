'''
Pandas Schema:
data = [[5, 'Alice', 250, 1], [4, 'Bob', 175, 5], [3, 'Alex', 350, 2], [6, 'John Cena', 400, 3], [1, 'Winston', 500, 6], [2, 'Marie', 200, 4]]
queue = pd.DataFrame(data, columns=['person_id', 'person_name', 'weight', 'turn']).astype({'person_id':'Int64', 'person_name':'object', 'weight':'Int64', 'turn':'Int64'})
'''

import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue.sort_values(by='turn', ascending=True, inplace=True)
    weight = 0
    last_person = None

    for i, row in queue.iterrows():
        if weight + row.weight <= 1000:
            weight += row.weight
            last_person = row.person_name
        else:
            return pd.DataFrame({'person_name': [last_person]})
        
    return pd.DataFrame({'person_name': [last_person]})
