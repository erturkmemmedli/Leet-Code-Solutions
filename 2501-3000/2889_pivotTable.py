import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = weather.pivot_table(values='temperature', index='month', columns='city')
    return df
