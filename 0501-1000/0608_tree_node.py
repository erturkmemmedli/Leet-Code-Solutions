'''
Pandas Schema:
data = [[1, None], [2, 1], [3, 1], [4, 2], [5, 2]]
tree = pd.DataFrame(data, columns=['id', 'p_id']).astype({'id':'Int64', 'p_id':'Int64'})
'''

import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    parents = set(tree['p_id'].unique())

    tree['type'] = 'Inner'
    tree.loc[~tree['id'].isin(parents), 'type'] = 'Leaf'
    tree.loc[tree['p_id'].isna(), 'type'] = 'Root'

    tree.drop(columns=['p_id'], inplace=True)

    return tree
