'''
Pandas Schema:
data = [[6, '2020-06-30 15:06:07'], [6, '2021-04-21 14:06:06'], [6, '2019-03-07 00:18:15'], [8, '2020-02-01 05:10:53'], [8, '2020-12-30 00:46:50'], [2, '2020-01-16 02:49:50'], [2, '2019-08-25 07:59:08'], [14, '2019-07-14 09:00:00'], [14, '2021-01-06 11:59:59']]
logins = pd.DataFrame(data, columns=['user_id', 'time_stamp']).astype({'user_id':'Int64', 'time_stamp':'datetime64[ns]'})
'''

import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins.sort_values(by='time_stamp', inplace=True)
    user_map = {}

    for i, r in logins.iterrows():
        if r['time_stamp'].year == 2020:
            user_map[r['user_id']] = r['time_stamp']
    
    return pd.DataFrame([(k, v) for k, v in user_map.items()], columns=['user_id', 'last_stamp'])
