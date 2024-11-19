'''
Pandas Schema:
data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30]]
prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype({'product_id':'Int64', 'start_date':'datetime64[ns]', 'end_date':'datetime64[ns]', 'price':'Int64'})
data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype({'product_id':'Int64', 'purchase_date':'datetime64[ns]', 'units':'Int64'})
'''

import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    units_sold.sort_values('product_id')
    product_map = {}
    output = {}

    for i, row in prices.iterrows():
        if row.product_id not in product_map:
            product_map[row.product_id] = []
            output[row.product_id] = [0, 0]
        product_map[row.product_id].append([row.start_date, row.end_date, row.price])
    
    for i, row in units_sold.iterrows():
        for item in product_map[row.product_id]:
            if item[0] <= row.purchase_date <= item[1]:
                output[row.product_id][0] += item[2] * row.units
                output[row.product_id][1] += row.units
                break
        
    df = pd.DataFrame({
        'product_id': k,
        'average_price': round(v[0] / v[1] if v[1] != 0 else 0, 2)
    } for k, v in output.items())

    return df
