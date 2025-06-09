'''
Pandas Schema:
data = [[1, 23], [2, 9], [4, 30], [5, 54], [6, 96], [7, 54], [8, 54]]
visits = pd.DataFrame(data, columns=['visit_id', 'customer_id']).astype({'visit_id':'Int64', 'customer_id':'Int64'})
data = [[2, 5, 310], [3, 5, 300], [9, 5, 200], [12, 1, 910], [13, 2, 970]]
transactions = pd.DataFrame(data, columns=['transaction_id', 'visit_id', 'amount']).astype({'transaction_id':'Int64', 'visit_id':'Int64', 'amount':'Int64'})
'''

import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    visited_trans = set(transactions['visit_id'])
    visited_no_trans = set(i for i in visits['visit_id'] if i not in visited_trans)
    output_dict = {}

    for i, row in visits.iterrows():
        if row['visit_id'] in visited_no_trans:
            output_dict[row['customer_id']] = output_dict.get(row['customer_id'], 0) + 1
    
    return pd.DataFrame(list(output_dict.items()), columns=['customer_id', 'count_no_trans'])
