'''
data = [[13, 15, 30], [10, 20, 15]]
triangle = pd.DataFrame(data, columns=['x', 'y', 'z']).astype({'x':'Int64', 'y':'Int64', 'z':'Int64'})
'''

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    f1 = triangle['x'] + triangle['y'] <= triangle['z']
    f2 = triangle['x'] + triangle['z'] <= triangle['y']
    f3 = triangle['y'] + triangle['z'] <= triangle['x']

    triangle['triangle'] = 'Yes'
    triangle.loc[f1 | f2 | f3, 'triangle'] = 'No'

    return triangle
