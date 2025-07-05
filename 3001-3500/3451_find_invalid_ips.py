'''
Pandas Schema:
data = [[1, '192.168.1.1', 200], [2, '256.1.2.3', 404], [3, '192.168.001.1', 200], [4, '192.168.1.1', 200], [5, '192.168.1', 500], [6, '256.1.2.3', 404], [7, '192.168.001.1', 200]]
logs = pd.DataFrame(columns=["log_id", "ip", "status_code"]).astype({"log_id": "Int64", "ip": "string", "status_code": "Int64"})
'''

import pandas as pd
from collections import Counter

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    count_map = Counter(logs['ip'])

    for k in list(count_map.keys()):
        if is_valid(k):
            del count_map[k]
    
    df = pd.DataFrame([(k, v) for k, v in count_map.items()], columns=['ip', 'invalid_count'])
    df.sort_values(by=['invalid_count', 'ip'], ascending=[0, 0], inplace=True)
    return df

def is_valid(ip: str) -> bool:
    octet = ip.split('.')
    
    if len(octet) != 4:
        return False
    
    if any(len(val) > 1 and val[0] == '0' for val in octet):
        return False
    
    if any(int(val) > 255 for val in octet):
        return False

    return True
