'''
Pandas Schema:
data = [[121, 'US', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'], [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype({'id':'Int64', 'country':'object', 'state':'object', 'amount':'Int64', 'trans_date':'datetime64[ns]'})
'''

import pandas as pd
from collections import defaultdict

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries.dropna(subset=['query_name'], inplace=True)
    query_map = {}

    for i, row in queries.iterrows():
        if row.query_name not in query_map:
            query_map[row.query_name] = defaultdict(int)
            query_map[row.query_name] = defaultdict(int)
    
        query_map[row.query_name]['quality'] += (row.rating / row.position)
        query_map[row.query_name]['count'] += 1

        if 'poor_query_count' not in query_map[row.query_name]:
            query_map[row.query_name]['poor_query_count'] = 0

        if row.rating < 3:
            query_map[row.query_name]['poor_query_count'] += 1
    
    df = pd.DataFrame({
        'query_name': k,
        'quality': round(v['quality'] / v['count'], 2),
        'poor_query_percentage': round(v['poor_query_count'] / v['count'] * 100, 2)
        } for k, v in query_map.items())

    return df
