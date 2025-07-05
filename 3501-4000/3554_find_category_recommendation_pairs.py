'''
Pandas Schedule:
data = [[1, 101, 2], [1, 102, 1], [1, 201, 3], [1, 301, 1], [2, 101, 1], [2, 102, 2], [2, 103, 1], [2, 201, 5], [3, 101, 2], [3, 103, 1], [3, 301, 4], [3, 401, 2], [4, 101, 1], [4, 201, 3], [4, 301, 1], [4, 401, 2], [5, 102, 2], [5, 103, 1], [5, 201, 2], [5, 202, 3]]
product_purchases = pd.DataFrame({
    "user_id": pd.Series(dtype='int64'),
    "product_id": pd.Series(dtype='int64'),
    "quantity": pd.Series(dtype='int64')
})
data = [[101, 'Electronics', 100], [102, 'Books', 20], [103, 'Books', 35], [201, 'Clothing', 45], [202, 'Clothing', 60], [301, 'Sports', 75], [401, 'Kitchen', 50]]
product_info= pd.DataFrame({
    "product_id": pd.Series(dtype='int64'),
    "category": pd.Series(dtype='string'),
    "price": pd.Series(dtype='float64')  # Reflects NUMBER(10, 2)
})
'''

import pandas as pd

def find_category_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    product_purchases = pd.merge(product_purchases, product_info, on='product_id', how='left')
    purchase_map = defaultdict(set)
    data = []
    
    for i, r in product_purchases.iterrows():
        purchase_map[r['category']].add(r['user_id'])

    items = sorted(purchase_map.keys())

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            intrsct = purchase_map[items[i]].intersection(purchase_map[items[j]])
            if len(intrsct) >= 3:
                data.append((items[i], items[j], len(intrsct)))
            
    df = pd.DataFrame(data, columns=['category1', 'category2', 'customer_count'])
    df.sort_values(by=['customer_count', 'category1', 'category2'], ascending=[0, 1, 1], inplace=True)
    return df
