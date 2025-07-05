'''
Pandas Schema:
data = [[1, '2023-01-01', 'free_trial', 45], [1, '2023-01-02', 'free_trial', 30], [1, '2023-01-05', 'free_trial', 60], [1, '2023-01-10', 'paid', 75], [1, '2023-01-12', 'paid', 90], [1, '2023-01-15', 'paid', 65], [2, '2023-02-01', 'free_trial', 55], [2, '2023-02-03', 'free_trial', 25], [2, '2023-02-07', 'free_trial', 50], [2, '2023-02-10', 'cancelled', 0], [3, '2023-03-05', 'free_trial', 70], [3, '2023-03-06', 'free_trial', 60], [3, '2023-03-08', 'free_trial', 80], [3, '2023-03-12', 'paid', 50], [3, '2023-03-15', 'paid', 55], [3, '2023-03-20', 'paid', 85], [4, '2023-04-01', 'free_trial', 40], [4, '2023-04-03', 'free_trial', 35], [4, '2023-04-05', 'paid', 45], [4, '2023-04-07', 'cancelled', 0]]
user_activity = pd.DataFrame({
    'user_id': pd.Series(dtype='int'),
    'activity_date': pd.Series(dtype='datetime64[ns]'),
    'activity_type': pd.Series(dtype='str'),
    'activity_duration': pd.Series(dtype='int')
})
'''

import pandas as pd
import numpy as np

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    hashmap = {}

    for i, r in user_activity.iterrows():
        if r['user_id'] not in hashmap:
            hashmap[r['user_id']] = [0, 0, 0, 0]
        if r['activity_type'] == 'free_trial':
            hashmap[r['user_id']][0] += 1
            hashmap[r['user_id']][1] += r['activity_duration']
        elif r['activity_type'] == 'paid':
            hashmap[r['user_id']][2] += 1
            hashmap[r['user_id']][3] += r['activity_duration']
    
    output = {'user_id': [], 'trial_avg_duration': [], 'paid_avg_duration': []}

    for k, v in hashmap.items():
        if v[2] != 0:
            output['user_id'].append(k)
            output['trial_avg_duration'].append(np.round(v[1]/v[0] + 0.0001, 2))
            output['paid_avg_duration'].append(np.round(v[3]/v[2] + 0.0001, 2))

    df = pd.DataFrame(output)
    df.sort_values(by='user_id')
    return df
