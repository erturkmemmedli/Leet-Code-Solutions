'''
Pandas Schema:
data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
'''

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, department, how='inner', left_on='departmentId', right_on='id')
    df.drop(['id_x', 'id_y', 'departmentId'], axis=1, inplace=True)
    df.rename(columns={"name_x": "Employee", "name_y": "Department", "salary": "Salary"}, inplace=True)

    order = [2,0,1]
    df = df[[df.columns[i] for i in order]]
    salaries = df["Salary"].to_list()

    max_salaries_for_departments = df.groupby("Department")["Salary"].agg('max').to_dict()
    df = df[[max_salaries_for_departments[df.loc[i, "Department"]] == salaries[i] for i in range(len(df))]]

    return df if len(df) else pd.DataFrame(columns=["Employee", "Department", "Salary"])
