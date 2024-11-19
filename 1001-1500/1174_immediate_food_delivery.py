'''
Pandas Schema:
data = [[1, 1, '2019-08-01', '2019-08-02'], [2, 2, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-12'], [4, 3, '2019-08-24', '2019-08-24'], [5, 3, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13'], [7, 4, '2019-08-09', '2019-08-09']]
delivery = pd.DataFrame(data, columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype({'delivery_id':'Int64', 'customer_id':'Int64', 'order_date':'datetime64[ns]', 'customer_pref_delivery_date':'datetime64[ns]'})
'''

import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery.sort_values(by='order_date', inplace=True)
    customers = set()
    immediate = 0
    scheduled = 0

    for i, row in delivery.iterrows():
        if row.customer_id not in customers:
            customers.add(row.customer_id)
            if row.order_date == row.customer_pref_delivery_date:
                immediate += 1
            else:
                scheduled += 1
            
    return pd.DataFrame({'immediate_percentage': [round(immediate / (immediate + scheduled) * 100, 2)]})
