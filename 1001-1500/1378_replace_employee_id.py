'''
Pandas Schema:
data = [['Leetcode', 'Buy', 1, 1000], ['Corona Masks', 'Buy', 2, 10], ['Leetcode', 'Sell', 5, 9000], ['Handbags', 'Buy', 17, 30000], ['Corona Masks', 'Sell', 3, 1010], ['Corona Masks', 'Buy', 4, 1000], ['Corona Masks', 'Sell', 5, 500], ['Corona Masks', 'Buy', 6, 1000], ['Handbags', 'Sell', 29, 7000], ['Corona Masks', 'Sell', 10, 10000]]
stocks = pd.DataFrame(data, columns=['stock_name', 'operation', 'operation_day', 'price']).astype({'stock_name':'object', 'operation':'object', 'operation_day':'Int64', 'price':'Int64'})
'''

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employees, employee_uni, on='id', how='left')
    return merged_df[['unique_id', 'name']]
