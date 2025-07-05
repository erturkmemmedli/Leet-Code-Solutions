'''
Pandas Schema:
data = [[1, 'Alice Smith', 28], [2, 'Bob Johnson', 35], [3, 'Carol Davis', 42], [4, 'David Wilson', 31], [5, 'Emma Brown', 29]]
patients = pd.DataFrame({
    'patient_id': pd.Series(dtype='int'),
    'patient_name': pd.Series(dtype='str'),
    'age': pd.Series(dtype='int')
})
data = [[1, 1, '2023-01-15', 'Positive'], [2, 1, '2023-01-25', 'Negative'], [3, 2, '2023-02-01', 'Positive'], [4, 2, '2023-02-05', 'Inconclusive'], [5, 2, '2023-02-12', 'Negative'], [6, 3, '2023-01-20', 'Negative'], [7, 3, '2023-02-10', 'Positive'], [8, 3, '2023-02-20', 'Negative'], [9, 4, '2023-01-10', 'Positive'], [10, 4, '2023-01-18', 'Positive'], [11, 5, '2023-02-15', 'Negative'], [12, 5, '2023-02-20', 'Negative']]
covid_tests = pd.DataFrame({
    'test_id': pd.Series(dtype='int'),
    'patient_id': pd.Series(dtype='int'),
    'test_date': pd.Series(dtype='datetime64[ns]'),
    'result': pd.Series(dtype='str')
})
'''

import pandas as pd

def find_covid_recovery_patients(patients: pd.DataFrame, covid_tests: pd.DataFrame) -> pd.DataFrame:
    covid_tests.sort_values(by='test_date')
    patients['recovery_time'] = None
    hashmap = {}
    
    for i, r in covid_tests.iterrows():
        if r['patient_id'] not in hashmap and r['result'] == 'Positive':
            hashmap[r['patient_id']] = r['test_date']
        
        if r['patient_id'] in hashmap and r['result'] == 'Negative':
            if pd.isna(patients.loc[patients['patient_id'] == r['patient_id'], 'recovery_time']).iloc[0]:
                diff = (pd.to_datetime(r['test_date']) - pd.to_datetime(hashmap[r['patient_id']])).days
                patients.loc[patients['patient_id'] == r['patient_id'], 'recovery_time'] = diff

    patients.dropna(subset=['recovery_time'], inplace=True)
    patients.sort_values(by=['recovery_time', 'patient_name'], ascending=[1, 1], inplace=True)
    return patients
