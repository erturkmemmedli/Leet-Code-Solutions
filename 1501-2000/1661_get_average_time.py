'''
Pandas Schema:
data = [[0, 0, 'start', 0.712], [0, 0, 'end', 1.52], [0, 1, 'start', 3.14], [0, 1, 'end', 4.12], [1, 0, 'start', 0.55], [1, 0, 'end', 1.55], [1, 1, 'start', 0.43], [1, 1, 'end', 1.42], [2, 0, 'start', 4.1], [2, 0, 'end', 4.512], [2, 1, 'start', 2.5], [2, 1, 'end', 5]]
activity = pd.DataFrame(data, columns=['machine_id', 'process_id', 'activity_type', 'timestamp']).astype({'machine_id':'Int64', 'process_id':'Int64', 'activity_type':'object', 'timestamp':'Float64'})
'''

import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    machine_map = {}

    for i, row in activity.iterrows():
        mid = row['machine_id']
        pid = row['process_id']
        at = row['activity_type']
        t = row['timestamp']
        if mid not in machine_map:
            machine_map[mid] = {}
        if pid not in machine_map[mid]:
            machine_map[mid][pid] = 0
        machine_map[mid][pid] += t if at == 'end' else -t

    output = {'machine_id': [], 'processing_time': []}

    for k, v in machine_map.items():
        output['machine_id'].append(k)
        output['processing_time'].append(round(sum(v.values())/len(v), 3))

    return pd.DataFrame(output)
