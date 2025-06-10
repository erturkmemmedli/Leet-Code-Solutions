'''
Pandas Schema:
data = [['2020-12-8', 'toyota', 0, 1], ['2020-12-8', 'toyota', 1, 0], ['2020-12-8', 'toyota', 1, 2], ['2020-12-7', 'toyota', 0, 2], ['2020-12-7', 'toyota', 0, 1], ['2020-12-8', 'honda', 1, 2], ['2020-12-8', 'honda', 2, 1], ['2020-12-7', 'honda', 0, 1], ['2020-12-7', 'honda', 1, 2], ['2020-12-7', 'honda', 2, 1]]
daily_sales = pd.DataFrame(data, columns=['date_id', 'make_name', 'lead_id', 'partner_id']).astype({'date_id':'datetime64[ns]', 'make_name':'object', 'lead_id':'Int64', 'partner_id':'Int64'})
'''

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    hashmap = {}

    for i, r in daily_sales.iterrows():
        pair = (r['date_id'], r['make_name'])
        if pair not in hashmap:
            hashmap[pair] = [set(), set()]
        hashmap[pair][0].add(r['lead_id'])
        hashmap[pair][1].add(r['partner_id'])

    output = {'date_id': [], 'make_name': [], 'unique_leads': [], 'unique_partners': []}
    
    for k, v in hashmap.items():
        output['date_id'].append(k[0])
        output['make_name'].append(k[1])
        output['unique_leads'].append(len(v[0]))
        output['unique_partners'].append(len(v[1]))

    return pd.DataFrame(output)
