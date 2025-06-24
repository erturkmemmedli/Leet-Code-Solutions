'''
data = [[3, 'Mila', 9, 60301], [12, 'Antonella', None, 31000], [13, 'Emery', None, 67084], [1, 'Kalel', 11, 21241], [9, 'Mikaela', None, 50937], [11, 'Joziah', 6, 28485]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'manager_id', 'salary']).astype({'employee_id':'Int64', 'name':'object', 'manager_id':'Int64', 'salary':'Int64'})
'''

import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    emp_set = set(employees['employee_id'])
    res = []

    for i, row in employees.iterrows():
        if row['salary'] < 30000 and pd.notna(row['manager_id']) and row['manager_id'] not in emp_set:
            res.append(row['employee_id'])
    
    return pd.DataFrame({'employee_id': sorted(res)})
