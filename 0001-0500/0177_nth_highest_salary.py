'''
Pandas Schema:
data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})
'''

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = sorted(employee['salary'].unique(), key = lambda x: -x)
    return pd.DataFrame({f'getNthHighestSalary({N})': [salaries[N - 1]] if len(salaries) > N - 1 else [None]})
