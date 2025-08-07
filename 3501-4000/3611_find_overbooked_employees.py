'''
Pandas Schema:
data = [[1, 'Alice Johnson', 'Engineering'], [2, 'Bob Smith', 'Marketing'], [3, 'Carol Davis', 'Sales'], [4, 'David Wilson', 'Engineering'], [5, 'Emma Brown', 'HR']]
employees = pd.DataFrame(columns=['employee_id', 'employee_name', 'department']).astype({'employee_id': 'Int64', 'employee_name': 'string', 'department': 'string'})

data = [[1, 1, '2023-06-05', 'Team', 8.0], [2, 1, '2023-06-06', 'Client', 6.0], [3, 1, '2023-06-07', 'Training', 7.0], [4, 1, '2023-06-12', 'Team', 12.0], [5, 1, '2023-06-13', 'Client', 9.0], [6, 2, '2023-06-05', 'Team', 15.0], [7, 2, '2023-06-06', 'Client', 8.0], [8, 2, '2023-06-12', 'Training', 10.0], [9, 3, '2023-06-05', 'Team', 4.0], [10, 3, '2023-06-06', 'Client', 3.0], [11, 4, '2023-06-05', 'Team', 25.0], [12, 4, '2023-06-19', 'Client', 22.0], [13, 5, '2023-06-05', 'Training', 2.0]]
meetings = pd.DataFrame(columns=['meeting_id', 'employee_id', 'meeting_date', 'meeting_type', 'duration_hours']).astype({'meeting_id': 'Int64', 'employee_id': 'Int64', 'meeting_date': 'datetime64[ns]', 'meeting_type': 'string', 'duration_hours': 'float64'})
'''

import pandas as pd

def find_overbooked_employees(employees: pd.DataFrame, meetings: pd.DataFrame) -> pd.DataFrame:
    meetings['week'] = meetings.meeting_date.dt.isocalendar().week

    df = meetings.groupby(['employee_id', 'week']).sum('duration_hours').reset_index()
    df = df.rename(columns = {'duration_hours': 'meeting_heavy_weeks'})
    df = df[df.meeting_heavy_weeks > 20.0].groupby(['employee_id']).count()
    df = df.merge(employees, on = 'employee_id')
    df = df[df.week > 1].sort_values(by=['meeting_heavy_weeks', 'employee_name'], ascending=[0,1])
    df = df[['employee_id', 'employee_name', 'department', 'meeting_heavy_weeks']]

    return df
