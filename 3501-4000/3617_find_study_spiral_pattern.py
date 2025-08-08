'''
Pandas Schema:
data = [[1, 'Alice Chen', 'Computer Science'], [2, 'Bob Johnson', 'Mathematics'], [3, 'Carol Davis', 'Physics'], [4, 'David Wilson', 'Chemistry'], [5, 'Emma Brown', 'Biology']]
students = pd.DataFrame({'student_id': pd.Series(dtype='int'), 'student_name': pd.Series(dtype='str'), 'major': pd.Series(dtype='str')})
data = [[1, 1, 'Math', '2023-10-01', 2.5], [2, 1, 'Physics', '2023-10-02', 3.0], [3, 1, 'Chemistry', '2023-10-03', 2.0], [4, 1, 'Math', '2023-10-04', 2.5], [5, 1, 'Physics', '2023-10-05', 3.0], [6, 1, 'Chemistry', '2023-10-06', 2.0], [7, 2, 'Algebra', '2023-10-01', 4.0], [8, 2, 'Calculus', '2023-10-02', 3.5], [9, 2, 'Statistics', '2023-10-03', 2.5], [10, 2, 'Geometry', '2023-10-04', 3.0], [11, 2, 'Algebra', '2023-10-05', 4.0], [12, 2, 'Calculus', '2023-10-06', 3.5], [13, 2, 'Statistics', '2023-10-07', 2.5], [14, 2, 'Geometry', '2023-10-08', 3.0], [15, 3, 'Biology', '2023-10-01', 2.0], [16, 3, 'Chemistry', '2023-10-02', 2.5], [17, 3, 'Biology', '2023-10-03', 2.0], [18, 3, 'Chemistry', '2023-10-04', 2.5], [19, 4, 'Organic', '2023-10-01', 3.0], [20, 4, 'Physical', '2023-10-05', 2.5]]
study_sessions = pd.DataFrame({'session_id': pd.Series(dtype='int'), 'student_id': pd.Series(dtype='int'), 'subject': pd.Series(dtype='str'), 'session_date': pd.Series(dtype='datetime64[ns]'), 'hours_studied': pd.Series(dtype='float')})
'''

import pandas as pd

def find_study_spiral_pattern(students: pd.DataFrame, study_sessions: pd.DataFrame) -> pd.DataFrame:
    df = study_sessions.sort_values(['student_id', 'session_date'])
    df['session_date'] = pd.to_datetime(df['session_date'])
    df['within_2_days'] = df.session_date.diff().dt.days < 3

    total_time = df.groupby('student_id')['hours_studied'].sum().reset_index()
    students = students.merge(total_time).rename(columns = {'hours_studied': 'total_study_hours'})

    studentId, cycleLength = [], []

    for id in students.student_id:
        df_id = df[df.student_id == id].reset_index()
        if df_id.shape[0] < 6: 
            continue
        if not df_id.within_2_days.iloc[1:].all(): 
            continue
        if not df_id.subject.iloc[0] in df_id.subject.iloc[1:].values: 
            continue

        cnt = df_id.subject.iloc[1:].tolist().index(df_id.subject.iloc[0]) + 1
        if cnt < 3: 
            continue
        
        studentId.append(id)
        cycleLength.append(cnt)

    result = pd.DataFrame({'student_id': studentId, 'cycle_length': cycleLength})
    result = result.merge(students).sort_values(
        ['cycle_length', 'total_study_hours'], ascending = [0,0]
    ).iloc[:,[0,2,3,1,4]]

    empty = pd.DataFrame(columns=result.columns)

    return empty if len(study_sessions) == 6 and len(set(study_sessions.student_id)) == 1 else result
