'''
Pandas Schema:
data = [[1, 2, '2016/06/03'], [1, 3, '2016/06/08'], [2, 3, '2016/06/08'], [3, 4, '2016/06/09']]
request_accepted = pd.DataFrame(data, columns=['requester_id', 'accepter_id', 'accept_date']).astype({'requester_id':'Int64', 'accepter_id':'Int64', 'accept_date':'datetime64[ns]'})
'''

import pandas as pd
from collections import Counter

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    friend_counter = Counter()
    
    for i, row in request_accepted.iterrows():
        friend_counter[row['requester_id']] += 1
        friend_counter[row['accepter_id']] += 1
    
    friend = None
    count = 0

    for k, v in friend_counter.items():
        if v > count:
            friend = k
            count = v
        
    return pd.DataFrame({'id': [friend], 'num': [count]})
