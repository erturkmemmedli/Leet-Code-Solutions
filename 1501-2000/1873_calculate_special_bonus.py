'''
Pandas Schedule:
data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})
'''

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    output = {'employee_id': [], 'bonus': []}

    for i, row in employees.iterrows():
        output['employee_id'].append(row['employee_id'])

        if row['employee_id'] % 2 == 1 and not row['name'].startswith('M'):
            output['bonus'].append(row['salary'])
        else:
            output['bonus'].append(0)
    
    df = pd.DataFrame(output)
    df.sort_values('employee_id', inplace=True)
    return df
