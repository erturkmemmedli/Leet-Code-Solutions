'''
Pandas Schedule:
data = [[0, 95, 100, 105], [1, 70, None, 80]]
products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype({'product_id':'Int64', 'store1':'Int64', 'store2':'Int64', 'store3':'Int64'})
'''

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    output = {'product_id': [], 'store': [], 'price': []}

    for i, row in products.iterrows():
        prod_id = None
        for k, v in row.items():
            if k == 'product_id':
                prod_id = v

            if k != 'product_id' and pd.notna(v):
                output['product_id'].append(prod_id)
                output['store'].append(k)
                output['price'].append(v)
            
    return pd.DataFrame(output)
