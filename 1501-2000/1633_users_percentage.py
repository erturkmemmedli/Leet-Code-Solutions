'''
Pandas Schema:
data = [[6, 'Alice'], [2, 'Bob'], [7, 'Alex']]
users = pd.DataFrame(data, columns=['user_id', 'user_name']).astype({'user_id':'Int64', 'user_name':'object'})
data = [[215, 6], [209, 2], [208, 2], [210, 6], [208, 6], [209, 7], [209, 6], [215, 7], [208, 7], [210, 2], [207, 2], [210, 7]]
register = pd.DataFrame(data, columns=['contest_id', 'user_id']).astype({'contest_id':'Int64', 'user_id':'Int64'})
'''

import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    user_set = set(users['user_id'])
    contest_counter = defaultdict(int)
    
    for i, r in register.iterrows():
        if r['user_id'] in user_set:
            contest_counter[r['contest_id']] += 1
    
    output = {'contest_id': [], 'percentage': []}

    for k, v in contest_counter.items():
        output['contest_id'].append(k)
        output['percentage'].append(round(v/len(user_set)*100, 2))

    result =  pd.DataFrame(output).sort_values(
        by=['percentage', 'contest_id'], 
        ascending=[False, True]
    )
    
    return result
