'''
Pandas Schema:
data = [['1', '2020-11-28', '4', '32'], ['1', '2020-11-28', '55', '200'], ['1', '2020-12-3', '1', '42'], ['2', '2020-11-28', '3', '33'], ['2', '2020-12-9', '47', '74']]
employees = pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time']).astype({'emp_id':'Int64', 'event_day':'datetime64[ns]', 'in_time':'Int64', 'out_time':'Int64'})
'''

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    hashmap = {}

    for i, r in employees.iterrows():
        pair = (r['emp_id'], r['event_day'])
        hashmap[pair] = hashmap.get(pair, 0) + (r['out_time'] - r['in_time'])

    output = {'day': [], 'emp_id': [], 'total_time': []}
    
    for k, v in hashmap.items():
        output['day'].append(k[1])
        output['emp_id'].append(k[0])
        output['total_time'].append(v)

    return pd.DataFrame(output)
