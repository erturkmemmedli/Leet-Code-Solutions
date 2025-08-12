'''
Pandas Schedule:
data = [[1, 'The Great Gatsby', 'F. Scott', 'Fiction', 180], [2, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction', 281], [3, '1984', 'George Orwell', 'Dystopian', 328], [4, 'Pride and Prejudice', 'Jane Austen', 'Romance', 432], [5, 'The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 277]]
books = pd.DataFrame({
    "book_id": pd.Series(dtype="int64"),      # SERIAL -> int64
    "title": pd.Series(dtype="string"),       # VARCHAR -> string dtype
    "author": pd.Series(dtype="string"),      # VARCHAR -> string dtype
    "genre": pd.Series(dtype="string"),       # VARCHAR -> string dtype
    "pages": pd.Series(dtype="int64")         # INTEGER -> int64
})
data = [[1, 1, 'Alice', 50, 5], [2, 1, 'Bob', 60, 1], [3, 1, 'Carol', 40, 4], [4, 1, 'David', 30, 2], [5, 1, 'Emma', 45, 5], [6, 2, 'Frank', 80, 4], [7, 2, 'Grace', 70, 4], [8, 2, 'Henry', 90, 5], [9, 2, 'Ivy', 60, 4], [10, 2, 'Jack', 75, 4], [11, 3, 'Kate', 100, 2], [12, 3, 'Liam', 120, 1], [13, 3, 'Mia', 80, 2], [14, 3, 'Noah', 90, 1], [15, 3, 'Olivia', 110, 4], [16, 3, 'Paul', 95, 5], [17, 4, 'Quinn', 150, 3], [18, 4, 'Ruby', 140, 3], [19, 5, 'Sam', 80, 1], [20, 5, 'Tara', 70, 2]]
reading_sessions = pd.DataFrame({
    "session_id": pd.Series(dtype="int64"),       # NUMBER -> int64
    "book_id": pd.Series(dtype="int64"),          # NUMBER -> int64
    "reader_name": pd.Series(dtype="string"),     # VARCHAR2 -> string dtype
    "pages_read": pd.Series(dtype="int64"),       # NUMBER -> int64
    "session_rating": pd.Series(dtype="int64")    # NUMBER -> int64
})
'''

import pandas as pd

def find_polarized_books(books: pd.DataFrame, reading_sessions: pd.DataFrame) -> pd.DataFrame:
    books['overall_count'] = 0
    books['low_count'] = 0
    books['high_count'] = 0
    books['min_rating'] = float('inf')
    books['max_rating'] = -float('inf')

    for i, row in reading_sessions.iterrows():
        books.loc[books.book_id == row.book_id, 'overall_count'] += 1
        books.loc[books.book_id == row.book_id, 'low_count'] += int(row.session_rating <= 2)
        books.loc[books.book_id == row.book_id, 'high_count'] += int(row.session_rating >= 4)
        minimum = books.loc[books.book_id == row.book_id, 'min_rating'].iloc[0]
        books.loc[books.book_id == row.book_id, 'min_rating'] = min(minimum, row.session_rating)
        maximum = books.loc[books.book_id == row.book_id, 'max_rating'].iloc[0]
        books.loc[books.book_id == row.book_id, 'max_rating'] = max(maximum, row.session_rating)

    books['rating_spread'] = books['max_rating'] - books['min_rating']
    books['polarization_score'] = (books['low_count'] + books['high_count']) / books['overall_count']

    df = books[
        (books['overall_count'] >= 5) &
        (books['polarization_score'] >= 0.6) &
        (books['rating_spread'] > 1) &
        (books['low_count'] >= 1) &
        (books['high_count'] >= 1)
    ]
    
    df['polarization_score'] = round(df['polarization_score'], 2)
    df.drop(columns=['overall_count', 'low_count', 'high_count', 'min_rating', 'max_rating'], inplace=True)
    df.sort_values(by=['polarization_score', 'title'], ascending=[0, 0], inplace=True)

    return df
