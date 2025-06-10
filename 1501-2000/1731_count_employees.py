'''
Pandas Schema:
data = [[9, 'Hercy', None, 43], [6, 'Alice', 9, 41], [4, 'Bob', 9, 36], [2, 'Winston', None, 37]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'reports_to', 'age']).astype({'employee_id':'Int64', 'name':'object', 'reports_to':'Int64', 'age':'Int64'})
'''

import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    report_map = defaultdict(list)

    for i, r in employees.iterrows():
        if pd.notna(r['reports_to']):
            report_map[r['reports_to']].append(r['age'])

    output = {'employee_id': [], 'name': [], 'reports_count': [], 'average_age': []}

    for i, r in employees.iterrows():
        if r['employee_id'] in report_map:
            total_age = sum(report_map[r['employee_id']])
            count_age = len(report_map[r['employee_id']])
            output['employee_id'].append(r['employee_id'])
            output['name'].append(r['name'])
            output['reports_count'].append(count_age)
            output['average_age'].append(round(total_age/count_age + 0.00001))

    output = pd.DataFrame(output)
    output.sort_values('employee_id', inplace=True)
    return output
