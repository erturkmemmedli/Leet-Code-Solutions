'''
Pandas Schema:
data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})
'''

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    category_map = {'Low Salary': 0, 'Average Salary': 0, 'High Salary': 0}

    for i, row in accounts.iterrows():
        if row['income'] < 20000:
            category_map['Low Salary'] += 1
        elif row['income'] > 50000:
            category_map['High Salary'] += 1
        else:
            category_map['Average Salary'] += 1
    
    columns = ['category', 'accounts_count']
    return pd.DataFrame([(k, v) for k, v in category_map.items()], columns=columns)
