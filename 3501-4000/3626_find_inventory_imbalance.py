'''
Pandas Schema:
data = [[1, 'Downtown Tech', 'New York'], [2, 'Suburb Mall', 'Chicago'], [3, 'City Center', 'Los Angeles'], [4, 'Corner Shop', 'Miami'], [5, 'Plaza Store', 'Seattle']]
stores = pd.DataFrame(data, columns=['store_id', 'store_name', 'location']).astype({'store_id': 'int64', 'store_name': 'string', 'location': 'string'})

data = [[1, 1, 'Laptop', 5, 999.99], [2, 1, 'Mouse', 50, 19.99], [3, 1, 'Keyboard', 25, 79.99], [4, 1, 'Monitor', 15, 299.99], [5, 2, 'Phone', 3, 699.99], [6, 2, 'Charger', 100, 25.99], [7, 2, 'Case', 75, 15.99], [8, 2, 'Headphones', 20, 149.99], [9, 3, 'Tablet', 2, 499.99], [10, 3, 'Stylus', 80, 29.99], [11, 3, 'Cover', 60, 39.99], [12, 4, 'Watch', 10, 299.99], [13, 4, 'Band', 25, 49.99], [14, 5, 'Camera', 8, 599.99], [15, 5, 'Lens', 12, 199.99]]
inventory = pd.DataFrame(data, columns=['inventory_id', 'store_id', 'product_name', 'quantity', 'price']).astype({'inventory_id': 'int64', 'store_id': 'int64', 'product_name': 'string', 'quantity': 'int64', 'price': 'float64'})
'''

import pandas as pd

def find_inventory_imbalance(stores: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    inventory.drop(columns=['inventory_id'], inplace=True)
    df = pd.merge(stores, inventory, on='store_id', how='right')
    
    store_counts = df['store_id'].value_counts()
    valid_store_ids = store_counts[store_counts >= 3].index
    df = df[df['store_id'].isin(valid_store_ids)]

    idx_max = df.groupby('store_id')['price'].idxmax()
    idx_min = df.groupby('store_id')['price'].idxmin()

    df_max = df.loc[idx_max].copy()
    df_min = df.loc[idx_min].copy()
    
    df_max = df_max.rename(columns={
        'price': 'price_max', 
        'quantity': 'quantity_max',
        'product_name': 'most_exp_product'
    })

    df_min = df_min.rename(columns={
        'price': 'price_min', 
        'quantity': 'quantity_min',
        'product_name': 'cheapest_product'
    })

    df_min.drop(columns=['store_name', 'location'], inplace=True)
    df = pd.merge(df_max, df_min, on='store_id')

    df['imbalance_ratio'] = round(df['quantity_min'] / df['quantity_max'], 2)
    df = df[df['quantity_max'] < df['quantity_min']]

    df.drop(columns=['quantity_max', 'quantity_min', 'price_max', 'price_min'], inplace=True)
    df.sort_values(by=['imbalance_ratio', 'store_name'], ascending=[False, True], inplace=True)
    return df
