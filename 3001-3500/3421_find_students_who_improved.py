'''
Pandas Schema:

data = [[101, 'Math', 70, '2023-01-15'], [101, 'Math', 85, '2023-02-15'], [101, 'Physics', 65, '2023-01-15'], [101, 'Physics', 60, '2023-02-15'], [102, 'Math', 80, '2023-01-15'], [102, 'Math', 85, '2023-02-15'], [103, 'Math', 90, '2023-01-15'], [104, 'Physics', 75, '2023-01-15'], [104, 'Physics', 85, '2023-02-15']]
scores = pd.DataFrame({"student_id": pd.Series(dtype="int"),
                          "subject": pd.Series(dtype="str"),
                          "score": pd.Series(dtype="int"),
                          "exam_date": pd.Series(dtype="str")})
'''

import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by='exam_date')
    hashmap = defaultdict(list)
    res = {'student_id': [], 'subject': [], 'first_score': [], 'latest_score': []}
    
    for i, r in scores.iterrows():
        sid = r['student_id']
        sub = r['subject']
        scr = r['score']
        hashmap[(sid, sub)].append(scr)

    for k, v in hashmap.items():
        if len(v) > 1 and v[-1] > v[0]:
            res['student_id'].append(k[0])
            res['subject'].append(k[1])
            res['first_score'].append(v[0])
            res['latest_score'].append(v[-1])
    
    df = pd.DataFrame(res)
    df = df.sort_values(by=['student_id', 'subject'])
    return df
