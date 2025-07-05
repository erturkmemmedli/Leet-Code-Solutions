'''
Pandas Schema:
data = [[1, 'hello world of SQL'], [2, 'the QUICK-brown fox'], [3, 'modern-day DATA science'], [4, 'web-based FRONT-end development']]
user_content = pd.DataFrame({
    'content_id': pd.Series(dtype='int'),
    'content_text': pd.Series(dtype='str')
})
'''

import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content['converted_text'] = user_content['content_text'].apply(capitalize)
    user_content.rename(columns={'content_text': 'original_text'}, inplace=True)
    return user_content
    
def capitalize(s: str) -> str:
    output = ""
    words = s.split()

    for word in words:
        final = word.split('-')
        res = "-".join(w.capitalize() for w in final) if len(final) > 1 else word.capitalize()
        output += (" " if output else "") + res

    return output
