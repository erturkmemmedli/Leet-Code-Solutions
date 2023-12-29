'''
Pandas Schema:
data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-03-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})
'''

import pandas as pd
import numpy as np

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    players = set()
    players_included = set()

    activity.sort_values(by='event_date', ascending=True, inplace=True)
    df = activity.groupby('event_date', as_index=False)['player_id'].agg(set = lambda x: set(x))
    
    for i, row in df.iterrows():
        if i > 0:
            if (row['event_date'] - df.loc[i-1]['event_date']).days == 1:
                for player in row['set']:
                    if player not in players and player in df.loc[i-1]['set']:
                        players_included.add(player)

            players |= df.loc[i-1]['set']

    players |= df.loc[len(df)-1]['set']

    return pd.DataFrame({'fraction' : np.round(len(players_included) / len(players), 2)}, index=[0])
