'''
Pandas Schema:
data = [[1, 101, 2], [1, 102, 1], [1, 103, 3], [2, 101, 1], [2, 102, 5], [2, 104, 1], [3, 101, 2], [3, 103, 1], [3, 105, 4], [4, 101, 1], [4, 102, 1], [4, 103, 2], [4, 104, 3], [5, 102, 2], [5, 104, 1]]
product_purchases = pd.DataFrame({
    "user_id": pd.Series(dtype='int64'),
    "product_id": pd.Series(dtype='int64'),
    "quantity": pd.Series(dtype='int64')
})
data = [[101, 'Electronics', 100], [102, 'Books', 20], [103, 'Clothing', 35], [104, 'Kitchen', 50], [105, 'Sports', 75]]
product_info= pd.DataFrame({
    "product_id": pd.Series(dtype='int64'),
    "category": pd.Series(dtype='string'),
    "price": pd.Series(dtype='float64')  # Reflects NUMBER(10, 2)
})
'''

import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    product_map = defaultdict(set)
    cat = {}
    
    for i, r in product_purchases.iterrows():
        product_map[r['product_id']].add(r['user_id'])

    for i, r in product_info.iterrows():
        cat[r['product_id']] = r['category']

    items = sorted(list(product_map.keys()))
    output = []

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            inter = product_map[items[i]].intersection(product_map[items[j]])
            if len(inter) >= 3:
                output.append((items[i], items[j], cat[items[i]], cat[items[j]], len(inter)))

    columns = ['product1_id', 'product2_id', 'product1_category', 'product2_category', 'customer_count']
    df = pd.DataFrame(output, columns=columns)
    df = df.sort_values(by=['customer_count', 'product1_id', 'product2_id'], ascending=[False, True, True])
    return df
