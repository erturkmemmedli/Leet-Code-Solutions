'''
Pandas Schema:
data = [[8], [8], [3], [3], [1], [4], [5], [6]]
my_numbers = pd.DataFrame(data, columns=['num']).astype({'num':'Int64'})
'''

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    count = my_numbers['num'].value_counts()
    count = count[count == 1]
    return pd.DataFrame({'num': [count.index.max()]})
