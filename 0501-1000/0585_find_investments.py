'''
Pandas Schema:
data = [[1, 10, 5, 10, 10], [2, 20, 20, 20, 20], [3, 10, 30, 20, 20], [4, 10, 40, 40, 40]]
insurance = pd.DataFrame(data, columns=['pid', 'tiv_2015', 'tiv_2016', 'lat', 'lon']).astype({'pid':'Int64', 'tiv_2015':'Float64', 'tiv_2016':'Float64', 'lat':'Float64', 'lon':'Float64'})
'''

import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    count = insurance['tiv_2015'].value_counts()
    count = count[count > 1]

    tiv_2015_filter = insurance['tiv_2015'].isin(set(count.keys()))
    lat_lon_filter = insurance.groupby(['lat', 'lon']).transform('size') == 1

    final_df = insurance[tiv_2015_filter & lat_lon_filter]

    return pd.DataFrame({"tiv_2016": [final_df['tiv_2016'].sum()]})
