'''
Pandas Schema:
data = [[1, 5], [2, 6], [3, 5], [3, 6], [1, 6]]
customer = pd.DataFrame(data, columns=['customer_id', 'product_key']).astype({'customer_id':'Int64', 'product_key':'Int64'})
data = [[5], [6]]
product = pd.DataFrame(data, columns=['product_key']).astype({'product_key':'Int64'})
'''

import pandas as pd
from collections import defaultdict

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    product = set(product['product_key'])

    customers = defaultdict(set)
    ids = []

    for i, row in customer.iterrows():
        customers[row['customer_id']].add(row['product_key'])
    
    for k, v in customers.items():
        if v == product:
            ids.append(k)

    return pd.DataFrame({'customer_id': ids})
