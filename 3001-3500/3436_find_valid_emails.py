'''
data = [[1, 'alice@example.com'], [2, 'bob_at_example.com'], [3, 'charlie@example.net'], [4, 'david@domain.com'], [5, 'eve@invalid']]
users = pd.DataFrame(columns=["user_id", "email"]).astype({"user_id": "int32", "email": "string"})
'''

import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['email'].apply(filterization)]

def filterization(email):
    if email.count('@') != 1:
        return False

    if not email.endswith('.com'):
        return False

    head, tail = email.split('@')

    if not head.isalnum() and head != '_':
        return False

    if not tail[:-4].isalpha():
        return False

    return True
