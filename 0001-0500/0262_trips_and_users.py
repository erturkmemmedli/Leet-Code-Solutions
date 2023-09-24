'''
Pandas Schema:
data = [['1', '1', '10', '1', 'completed', '2013-10-01'], ['2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01'], ['3', '3', '12', '6', 'completed', '2013-10-01'], ['4', '4', '13', '6', 'cancelled_by_client', '2013-10-01'], ['5', '1', '10', '1', 'completed', '2013-10-02'], ['6', '2', '11', '6', 'completed', '2013-10-02'], ['7', '3', '12', '6', 'completed', '2013-10-02'], ['8', '2', '12', '12', 'completed', '2013-10-03'], ['9', '3', '10', '12', 'completed', '2013-10-03'], ['10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03']]
trips = pd.DataFrame(data, columns=['id', 'client_id', 'driver_id', 'city_id', 'status', 'request_at']).astype({'id':'Int64', 'client_id':'Int64', 'driver_id':'Int64', 'city_id':'Int64', 'status':'object', 'request_at':'object'})

data = [['1', 'No', 'client'], ['2', 'Yes', 'client'], ['3', 'No', 'client'], ['4', 'No', 'client'], ['10', 'No', 'driver'], ['11', 'No', 'driver'], ['12', 'No', 'driver'], ['13', 'No', 'driver']]
users = pd.DataFrame(data, columns=['users_id', 'banned', 'role']).astype({'users_id':'Int64', 'banned':'object', 'role':'object'})
'''

import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    banned = set()

    for idx, row in users.iterrows():
        if row['banned'] == 'Yes':
            banned.add(row['users_id'])

    trips = trips[~trips['client_id'].isin(banned) & ~trips['driver_id'].isin(banned)]
    trips['request_at'] = pd.to_datetime(trips['request_at'])
    trips = trips[(pd.to_datetime("2013-10-01") <= trips['request_at']) & (trips['request_at'] <= pd.to_datetime("2013-10-03"))]

    pivot = trips.pivot_table(index='request_at', columns='status', values='id', aggfunc='count', fill_value=0)

    pivot.reset_index(inplace=True)
    pivot.rename(columns={'request_at' : "Day"}, inplace=True)
    
    for col_name in ['cancelled_by_client', 'cancelled_by_driver', 'completed']:
        if col_name not in pivot.columns:
            pivot[col_name] = [0] * pivot.shape[0]

    pivot['total'] = pivot['cancelled_by_client'] + pivot['cancelled_by_driver'] + pivot['completed']
    pivot['Cancellation Rate'] = ((pivot['total'] - pivot['completed']) / pivot['total']).round(2)

    pivot = pivot[['Day', 'Cancellation Rate']]

    return pivot
