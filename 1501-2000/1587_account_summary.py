'''
Pandas Schema:
data = [[900001, 'Alice'], [900002, 'Bob'], [900003, 'Charlie']]
users = pd.DataFrame(data, columns=['account', 'name']).astype({'account':'Int64', 'name':'object'})
data = [[1, 900001, 7000, '2020-08-01'], [2, 900001, 7000, '2020-09-01'], [3, 900001, -3000, '2020-09-02'], [4, 900002, 1000, '2020-09-12'], [5, 900003, 6000, '2020-08-07'], [6, 900003, 6000, '2020-09-07'], [7, 900003, -4000, '2020-09-11']]
transactions = pd.DataFrame(data, columns=['trans_id', 'account', 'amount', 'transacted_on']).astype({'trans_id':'Int64', 'account':'Int64', 'amount':'Int64', 'transacted_on':'datetime64[ns]'})
'''

import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    acc_map = {}

    for i, row in users.iterrows():
        acc_map[row['account']] = [row['name'], 0]
        
    for i, row in transactions.iterrows():
        acc_map[row['account']][1] += row['amount']

    output = {'name': [], 'balance': []}

    for k, v in acc_map.items():
        if v[1] > 10000:
            output['name'].append(v[0])
            output['balance'].append(v[1])

    return pd.DataFrame(output)
