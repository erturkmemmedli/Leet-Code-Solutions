'''
Pandas Schema:
data = [[3, '2020-03-21 10:16:13'], [7, '2020-01-04 13:57:59'], [2, '2020-07-29 23:09:44'], [6, '2020-12-09 10:39:37']]
signups = pd.DataFrame(data, columns=['user_id', 'time_stamp']).astype({'user_id':'Int64', 'time_stamp':'datetime64[ns]'})
data = [[3, '2021-01-06 03:30:46', 'timeout'], [3, '2021-07-14 14:00:00', 'timeout'], [7, '2021-06-12 11:57:29', 'confirmed'], [7, '2021-06-13 12:58:28', 'confirmed'], [7, '2021-06-14 13:59:27', 'confirmed'], [2, '2021-01-22 00:00:00', 'confirmed'], [2, '2021-02-28 23:59:59', 'timeout']]
confirmations = pd.DataFrame(data, columns=['user_id', 'time_stamp', 'action']).astype({'user_id':'Int64', 'time_stamp':'datetime64[ns]', 'action':'object'})
'''

import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    user_map = {ID: 0.00 for ID in signups['user_id']}
    user_count = {}
    confirmed_count = {}

    for i, r in confirmations.iterrows():
        user_count[r['user_id']] = user_count.get(r['user_id'], 0) + 1
        if r['action'] == 'confirmed':
            confirmed_count[r['user_id']] = confirmed_count.get(r['user_id'], 0) + 1
    
    for k in user_map.keys():
        if k in user_count:
            user_map[k] = round(confirmed_count.get(k, 0) / user_count[k], 2)
    
    columns = ['user_id', 'confirmation_rate']
    return pd.DataFrame([(k, v) for k, v in user_map.items()], columns=columns)
