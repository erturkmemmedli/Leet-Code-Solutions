'''
Pandas Schedule:
data = [['1', '1', 'N'], ['2', '1', 'Y'], ['2', '2', 'N'], ['3', '3', 'N'], ['4', '2', 'N'], ['4', '3', 'Y'], ['4', '4', 'N']]
employee = pd.DataFrame(data, columns=['employee_id', 'department_id', 'primary_flag']).astype({'employee_id':'Int64', 'department_id':'Int64', 'primary_flag':'object'})
'''

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee_map = {}
    output = {'employee_id': [], 'department_id': []}

    for i, r in employee.iterrows():
        if r['primary_flag'] == 'Y':
            employee_map[r['employee_id']] = r['department_id']
        elif r['employee_id'] not in employee_map:
            employee_map[r['employee_id']] = r['department_id']

    for k, v in employee_map.items():
        output['employee_id'].append(k)
        output['department_id'].append(v)

    return pd.DataFrame(output)
