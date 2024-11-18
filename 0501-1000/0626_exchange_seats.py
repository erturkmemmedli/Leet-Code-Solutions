'''
Pandas Schema:
data = [[1, 'Abbot'], [2, 'Doris'], [3, 'Emerson'], [4, 'Green'], [5, 'Jeames']]
seat = pd.DataFrame(data, columns=['id', 'student']).astype({'id':'Int64', 'student':'object'})
'''

import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    student = seat.student
    for i in range(1, len(student), 2):
        student[i], student[i - 1] = student[i - 1], student[i]
    seat['student'] = student
    return seat
