'''
Pandas Schema:
data = [[1, 'ATGCTAGCTAGCTAA', 'Human'], [2, 'GGGTCAATCATC', 'Human'], [3, 'ATATATCGTAGCTA', 'Human'], [4, 'ATGGGGTCATCATAA', 'Mouse'], [5, 'TCAGTCAGTCAG', 'Mouse'], [6, 'ATATCGCGCTAG', 'Zebrafish'], [7, 'CGTATGCGTCGTA', 'Zebrafish']]
samples = pd.DataFrame({
    'sample_id': pd.Series(dtype='int'),        # Equivalent to SERIAL/INTEGER
    'dna_sequence': pd.Series(dtype='string'),  # Equivalent to TEXT/VARCHAR
    'species': pd.Series(dtype='string')        # Equivalent to VARCHAR(100)
})
'''

import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples['has_start'] = samples['dna_sequence'].apply(has_start)
    samples['has_stop'] = samples['dna_sequence'].apply(has_stop)
    samples['has_atat'] = samples['dna_sequence'].apply(has_atat)
    samples['has_ggg'] = samples['dna_sequence'].apply(has_ggg)
    return samples

def has_start(dna: str) -> int:
    return int(dna[:3] == 'ATG')

def has_stop(dna: str) -> int:
    return int(dna[-3:] in ['TAA', 'TAG', 'TGA'])

def has_atat(dna: str) -> int:
    return int('ATAT' in dna)

def has_ggg(dna: str) -> int:
    return int('GGG' in dna)
