'''
Pandas Schema:
data = [['Leetcode', 'Buy', 1, 1000], ['Corona Masks', 'Buy', 2, 10], ['Leetcode', 'Sell', 5, 9000], ['Handbags', 'Buy', 17, 30000], ['Corona Masks', 'Sell', 3, 1010], ['Corona Masks', 'Buy', 4, 1000], ['Corona Masks', 'Sell', 5, 500], ['Corona Masks', 'Buy', 6, 1000], ['Handbags', 'Sell', 29, 7000], ['Corona Masks', 'Sell', 10, 10000]]
stocks = pd.DataFrame(data, columns=['stock_name', 'operation', 'operation_day', 'price']).astype({'stock_name':'object', 'operation':'object', 'operation_day':'Int64', 'price':'Int64'})
'''

import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stock_map = {}

    for i, row in stocks.iterrows():
        price = row['price'] if row['operation'] == 'Sell' else -row['price']
        stock_map[row['stock_name']] = stock_map.get(row['stock_name'], 0) + price

    return pd.DataFrame(list(stock_map.items()), columns=['stock_name', 'capital_gain_loss'])
