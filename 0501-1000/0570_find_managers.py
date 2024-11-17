'''
Pandas Scheme:
data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})
'''

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    gr = employee.groupby('managerId')[['id']].agg('count')
    gr = gr[gr['id'] >= 5]
    managers = set(gr.index.tolist())
    return employee[employee['id'].isin(managers)][['name']]
