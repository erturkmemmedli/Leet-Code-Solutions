'''
Pandas Schema:
data = [[1, 'Jhon', '2019-01-01', 100], [2, 'Daniel', '2019-01-02', 110], [3, 'Jade', '2019-01-03', 120], [4, 'Khaled', '2019-01-04', 130], [5, 'Winston', '2019-01-05', 110], [6, 'Elvis', '2019-01-06', 140], [7, 'Anna', '2019-01-07', 150], [8, 'Maria', '2019-01-08', 80], [9, 'Jaze', '2019-01-09', 110], [1, 'Jhon', '2019-01-10', 130], [3, 'Jade', '2019-01-10', 150]]
customer = pd.DataFrame(data, columns=['customer_id', 'name', 'visited_on', 'amount']).astype({'customer_id':'Int64', 'name':'object', 'visited_on':'datetime64[ns]', 'amount':'Int64'})
'''

import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer.groupby(['visited_on'])[['amount']].agg(amount=('amount', 'sum')).reset_index()
    df.sort_values('visited_on', inplace=True)

    visited_on = []
    amount = []
    window_sum = 0

    for i, row in df.iterrows():
        window_sum += row.amount
        if i == 6:
            amount.append(window_sum)
            visited_on.append(row.visited_on)
        elif i > 6:
            window_sum -= df.iloc[i-7]['amount']
            amount.append(window_sum)
            visited_on.append(row.visited_on)

    return pd.DataFrame({
        'visited_on': visited_on,
        'amount': amount,
        'average_amount': [round(i/7, 2) for i in amount]
    })
        



        


