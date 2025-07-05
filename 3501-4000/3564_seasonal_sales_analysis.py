'''
Pandas Schedule:
data = [[1, 1, '2023-01-15', 5, 10.0], [2, 2, '2023-01-20', 4, 15.0], [3, 3, '2023-03-10', 3, 18.0], [4, 4, '2023-04-05', 1, 20.0], [5, 1, '2023-05-20', 2, 10.0], [6, 2, '2023-06-12', 4, 15.0], [7, 5, '2023-06-15', 5, 12.0], [8, 3, '2023-07-24', 2, 18.0], [9, 4, '2023-08-01', 5, 20.0], [10, 5, '2023-09-03', 3, 12.0], [11, 1, '2023-09-25', 6, 10.0], [12, 2, '2023-11-10', 4, 15.0], [13, 3, '2023-12-05', 6, 18.0], [14, 4, '2023-12-22', 3, 20.0], [15, 5, '2024-02-14', 2, 12.0]]
sales = pd.DataFrame(columns=['sale_id', 'product_id', 'sale_date', 'quantity', 'price']).astype({'sale_id': 'int64', 'product_id': 'int64', 'sale_date': 'datetime64[ns]', 'quantity': 'int64', 'price': 'float64'})

data = [[1, 'Warm Jacket', 'Apparel'], [2, 'Designer Jeans', 'Apparel'], [3, 'Cutting Board', 'Kitchen'], [4, 'Smart Speaker', 'Tech'], [5, 'Yoga Mat', 'Fitness']]
products = pd.DataFrame(columns=['product_id', 'product_name', 'category']).astype({'product_id': 'int64', 'product_name': 'string', 'category': 'string'})
'''

import pandas as pd

def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    prod_cat_map = {}
    season_map = {'Fall': {}, 'Spring': {}, 'Summer': {}, 'Winter': {}}

    for i, r in products.iterrows():
        prod_cat_map[r['product_id']] = r['category']

    for i, r in sales.iterrows():
        if r['sale_date'].month in [12, 1, 2]:
            season = 'Winter'
        elif r['sale_date'].month in [3, 4, 5]:
            season = 'Spring'
        elif r['sale_date'].month in [6, 7, 8]:
            season = 'Summer'
        else:
            season = 'Fall'

        cat = prod_cat_map[r['product_id']]
        if cat not in season_map[season]:
            season_map[season][cat] = [0, 0]
        season_map[season][cat][0] += r['quantity']
        season_map[season][cat][1] += r['quantity'] * r['price']
    
    output = []

    for season, val in season_map.items():
        category = None
        total_quantity = total_revenue = 0

        for k, v in val.items():
            if v[0] > total_quantity:
                category = k
                total_quantity = v[0]
                total_revenue = v[1]
            elif v[0] == total_quantity and v[1] > total_revenue:
                category = k
                total_revenue = v[1]

        output.append((season, category, total_quantity, total_revenue))
    
    df = pd.DataFrame(output, columns=['season', 'category', 'total_quantity', 'total_revenue'])
    df.sort_values(by='season')
    return df
