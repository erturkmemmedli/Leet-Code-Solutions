'''
data = [[2, 'Crew'], [4, 'Haven'], [5, 'Kristian']]
employees = pd.DataFrame(data, columns=['employee_id', 'name']).astype({'employee_id':'Int64', 'name':'object'})
data = [[5, 76071], [1, 22517], [4, 63539]]
salaries = pd.DataFrame(data, columns=['employee_id', 'salary']).astype({'employee_id':'Int64', 'salary':'Int64'})
'''

import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employees, salaries, on='employee_id', how='outer')
    res = []

    for i, row in df.iterrows():
        if pd.isna(row['name']) or pd.isna(row['salary']):
            res.append(row['employee_id'])

    return pd.DataFrame({'employee_id': res})
