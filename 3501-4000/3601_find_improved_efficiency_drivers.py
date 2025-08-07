'''
Pandas Schema:
data = [[1, 'Alice Johnson'], [2, 'Bob Smith'], [3, 'Carol Davis'], [4, 'David Wilson'], [5, 'Emma Brown']]
drivers = pd.DataFrame({
    'driver_id': pd.Series(dtype='int'),
    'driver_name': pd.Series(dtype='str')
})
data = [[1, 1, '2023-02-15', 120.5, 10.2], [2, 1, '2023-03-20', 200.0, 16.5], [3, 1, '2023-08-10', 150.0, 11.0], [4, 1, '2023-09-25', 180.0, 12.5], [5, 2, '2023-01-10', 100.0, 9.0], [6, 2, '2023-04-15', 250.0, 22.0], [7, 2, '2023-10-05', 200.0, 15.0], [8, 3, '2023-03-12', 80.0, 8.5], [9, 3, '2023-05-18', 90.0, 9.2], [10, 4, '2023-07-22', 160.0, 12.8], [11, 4, '2023-11-30', 140.0, 11.0], [12, 5, '2023-02-28', 110.0, 11.5]]
trips = pd.DataFrame({
    'trip_id': pd.Series(dtype='int'),
    'driver_id': pd.Series(dtype='int'),
    'trip_date': pd.Series(dtype='datetime64[ns]'),
    'distance_km': pd.Series(dtype='float'),
    'fuel_consumed': pd.Series(dtype='float')
})
'''

import pandas as pd

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    trips['trip_date'] = pd.to_datetime(trips['trip_date'])
    driver_map = {row['driver_id']: [row['driver_name'], 0, 0, 0, 0] for i, row in drivers.iterrows()}

    for i, row in trips.iterrows():
        dr = driver_map[row['driver_id']]
        if row['trip_date'].month < 7:
            dr[1] += row['distance_km'] / row['fuel_consumed']
            dr[2] += 1
        else:
            dr[3] += row['distance_km'] / row['fuel_consumed']
            dr[4] += 1
        
    df = pd.DataFrame(columns=[
        "driver_id", "driver_name", "first_half_avg", "second_half_avg", "efficiency_improvement"
    ])

    for k, v in driver_map.items():
        if v[2] > 0 and v[4] > 0:
            left = v[1] / v[2]
            right = v[3] / v[4]
            diff = right - left
            if right - left > 0:
                df.loc[len(df)] = [k, v[0], round(left, 2), round(right, 2), round(diff, 2)]

    df = df.sort_values(by='efficiency_improvement', ascending=0)
    return df
