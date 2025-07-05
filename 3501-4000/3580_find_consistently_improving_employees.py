'''
Pandas Schema:
data = [[1, 'Alice Johnson'], [2, 'Bob Smith'], [3, 'Carol Davis'], [4, 'David Wilson'], [5, 'Emma Brown']]
employees = pd.DataFrame({
    'employee_id': pd.Series(dtype='int'),
    'name': pd.Series(dtype='str')
})
data = [[1, 1, '2023-01-15', 2], [2, 1, '2023-04-15', 3], [3, 1, '2023-07-15', 4], [4, 1, '2023-10-15', 5], [5, 2, '2023-02-01', 3], [6, 2, '2023-05-01', 2], [7, 2, '2023-08-01', 4], [8, 2, '2023-11-01', 5], [9, 3, '2023-03-10', 1], [10, 3, '2023-06-10', 2], [11, 3, '2023-09-10', 3], [12, 3, '2023-12-10', 4], [13, 4, '2023-01-20', 4], [14, 4, '2023-04-20', 4], [15, 4, '2023-07-20', 4], [16, 5, '2023-02-15', 3], [17, 5, '2023-05-15', 2]]
performance_reviews = pd.DataFrame({
    'review_id': pd.Series(dtype='int'),
    'employee_id': pd.Series(dtype='int'),
    'review_date': pd.Series(dtype='datetime64[ns]'),
    'rating': pd.Series(dtype='float')  # Use float to accommodate decimal ratings
})
'''

import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    employees['improvement_score'] = None
    performance_reviews.sort_values(by='review_date')
    hashmap = defaultdict(list)

    for i, r in performance_reviews.iterrows():
        hashmap[r['employee_id']].append(r['rating'])
    
    for k, v in hashmap.items():
        if len(v) >= 3 and v[-3] < v[-2] < v[-1]:
            employees.loc[employees['employee_id'] == k, 'improvement_score'] = v[-1] - v[-3]

    employees = employees.dropna(subset=['improvement_score'])
    employees = employees.sort_values(by=['improvement_score', 'name'], ascending=[0, 1])
    return employees
