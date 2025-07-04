'''
Pandas Schema:
data = [[1, 'Widget A', 'This is a sample product with SN1234-5678'], [2, 'Widget B', 'A product with serial SN9876-1234 in the description'], [3, 'Widget C', 'Product SN1234-56789 is available now'], [4, 'Widget D', 'No serial number here'], [5, 'Widget E', 'Check out SN4321-8765 in this description']]
products = pd.DataFrame(columns=['product_id', 'product_name', 'description']).astype({'product_id': 'int32', 'product_name': 'string', 'description': 'string'})
'''

import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[products['description'].apply(is_valid)]

def is_valid(desc: str) -> bool:
    words = desc.split()

    for word in words:
        if len(word) != 11:
            continue
        if word[:2] != 'SN':
            continue
        if not word[2:6].isdigit():
            continue
        if word[6] != '-':
            continue
        if not word[7:].isdigit():
            continue

        return True

    return False
