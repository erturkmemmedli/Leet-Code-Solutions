'''
data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})
'''

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    hashmap = defaultdict(set)

    for i, r in teacher.iterrows():
        hashmap[r['teacher_id']].add(r['subject_id'])
    
    return pd.DataFrame({'teacher_id': hashmap.keys(), 'cnt': [len(v) for v in hashmap.values()]})
