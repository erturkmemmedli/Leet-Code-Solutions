'''
Pandas Schema:
data = [['Dog', 'Golden Retriever', 1, 5], ['Dog', 'German Shepherd', 2, 5], ['Dog', 'Mule', 200, 1], ['Cat', 'Shirazi', 5, 2], ['Cat', 'Siamese', 3, 3], ['Cat', 'Sphynx', 7, 4]]
queries = pd.DataFrame(data, columns=['query_name', 'result', 'position', 'rating']).astype({'query_name':'object', 'result':'object', 'position':'Int64', 'rating':'Int64'})
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
