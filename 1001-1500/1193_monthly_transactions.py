'''
Pandas Schema:
data = [[121, 'US', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'], [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype({'id':'Int64', 'country':'object', 'state':'object', 'amount':'Int64', 'trans_date':'datetime64[ns]'})
'''

import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['trans_date'] = transactions['trans_date'].dt.strftime('%Y-%m')
    transactions['state'] = transactions['state'].map({'approved': 1, 'declined': 0})

    df = transactions.groupby(['country', 'trans_date'], dropna=False).agg(
        month=('trans_date', 'first'),
        country=('country', 'first'),
        trans_count=('country', 'size'),
        approved_count=('state', 'sum'),
        trans_total_amount=('amount', 'sum'),
        approved_total_amount=('amount', lambda x: x[transactions['state'] == 1].sum())
    )

    return df
