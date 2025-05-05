'''
Pandas Schema:
data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'], [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'], [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'], [7, 'Shapiro', '.shapo@leetcode.com']]
users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})
'''

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    indices = set()

    for i, row in users.iterrows():
        mail = row['mail'].split('@')

        if len(mail) != 2 or mail[1] != 'leetcode.com' or not mail[0][0].isalpha():
            continue

        flag = False
        for char in mail[0]:
            if not char.isalnum() and char not in '-._':
                flag = True
                break 
            
        if not flag:
            indices.add(i)

    return users.loc[users.index.isin(indices)]
