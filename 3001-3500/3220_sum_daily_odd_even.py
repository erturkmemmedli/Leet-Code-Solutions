'''
data = [[1, 150, '2024-07-01'], [2, 200, '2024-07-01'], [3, 75, '2024-07-01'], [4, 300, '2024-07-02'], [5, 50, '2024-07-02'], [6, 120, '2024-07-03']]
transactions = pd.DataFrame(
    columns=["transaction_id", "amount", "transaction_date"],
    dtype={
        "transaction_id": "int",
        "amount": "int",
        "transaction_date": "datetime64[ns]",
    },
)
'''

import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    transaction_map = {}
    output = {'transaction_date': [], 'odd_sum': [], 'even_sum': []}

    for i, r in transactions.iterrows():
        if r['transaction_date'] not in transaction_map:
            transaction_map[r['transaction_date']] = [0, 0]
        if r['amount'] % 2 == 0:
            transaction_map[r['transaction_date']][1] += r['amount']
        else:
            transaction_map[r['transaction_date']][0] += r['amount']
    
    for k, v in transaction_map.items():
        output['transaction_date'].append(k)
        output['odd_sum'].append(v[0])
        output['even_sum'].append(v[1])

    return pd.DataFrame(output).sort_values('transaction_date')
