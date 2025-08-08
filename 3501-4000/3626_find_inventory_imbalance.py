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
