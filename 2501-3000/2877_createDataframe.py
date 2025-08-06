import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame([{'student_id': i[0], 'age': i[1]} for i in student_data])
