'''
Pandas Schedule:
data = [[1, 'Alice', None, 12000, 'Executive'], [2, 'Bob', 1, 10000, 'Sales'], [3, 'Charlie', 1, 10000, 'Engineering'], [4, 'David', 2, 7500, 'Sales'], [5, 'Eva', 2, 7500, 'Sales'], [6, 'Frank', 3, 9000, 'Engineering'], [7, 'Grace', 3, 8500, 'Engineering'], [8, 'Hank', 4, 6000, 'Sales'], [9, 'Ivy', 6, 7000, 'Engineering'], [10, 'Judy', 6, 7000, 'Engineering']]
employees = pd.DataFrame(columns=["employee_id", "employee_name", "manager_id", "salary", "department"]).astype({"employee_id": "int", "employee_name": "string", "manager_id": "Int64", "salary": "int", "department": "string"})
'''

import pandas as pd
from collections import deque, defaultdict

def analyze_organization_hierarchy(employees: pd.DataFrame) -> pd.DataFrame:
    employee_salary_name_map = {}
    graph = defaultdict(list)
    employee_map = {}
    root_employee = None

    for i, r in employees.iterrows():
        employee_salary_name_map[r['employee_id']] = (r['salary'], r['employee_name'])

        if pd.isna(r['manager_id']):
            root_employee = r['employee_id']
        else:
            graph[r['manager_id']].append(r['employee_id'])
    
    def dfs(employee_id, level):
        size = 0
        budget = employee_salary_name_map[employee_id][0]

        if employee_id not in graph:
            employee_map[employee_id] = [level, size, budget]
            return employee_map[employee_id]
        
        for child in graph[employee_id]:
            l, s, b = dfs(child, level + 1)
            size += s + 1
            budget += b
        
        employee_map[employee_id] = [level, size, budget]
        return employee_map[employee_id]

    dfs(root_employee, 1)

    data = pd.DataFrame(
        [(k, employee_salary_name_map[k][1], v[0], v[1], v[2]) for k, v in employee_map.items()],
        columns=['employee_id', 'employee_name', 'level', 'team_size', 'budget']
    )

    data.sort_values(by=['level', 'budget', 'employee_name'], ascending=[1, 0, 1], inplace=True)
    return data
