'''
Pandas Schema:
data = [[1, 20, '2019-08-14'], [2, 50, '2019-08-14'], [1, 30, '2019-08-15'], [1, 35, '2019-08-16'], [2, 65, '2019-08-17'], [3, 20, '2019-08-18']]
products = pd.DataFrame(data, columns=['product_id', 'new_price', 'change_date']).astype({'product_id':'Int64', 'new_price':'Int64', 'change_date':'datetime64[ns]'})
'''

import pandas as pd
from datetime import datetime

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    products.sort_values(by='change_date', inplace=True)
    date = datetime(2019, 8, 16)
    id_price_map = {}

    for i, row in products.iterrows():
        if row.change_date <= date:
            id_price_map[row.product_id] = row.new_price
        elif row.product_id not in id_price_map:
            id_price_map[row.product_id] = 10
        
    result = pd.DataFrame({'product_id': id_price_map.keys(), 'price': id_price_map.values()})
    return result.sort_values(by='price')
