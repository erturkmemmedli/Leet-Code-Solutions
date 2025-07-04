'''
Pandas Schema:

data = [[1, 'The Great Gatsby', 'F. Scott', 'Fiction', 1925, 3], [2, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960, 3], [3, '1984', 'George Orwell', 'Dystopian', 1949, 1], [4, 'Pride and Prejudice', 'Jane Austen', 'Romance', 1813, 2], [5, 'The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951, 1], [6, 'Brave New World', 'Aldous Huxley', 'Dystopian', 1932, 4]]
library_books = pd.DataFrame({
    'book_id': pd.Series(dtype='int'),
    'title': pd.Series(dtype='str'),
    'author': pd.Series(dtype='str'),
    'genre': pd.Series(dtype='str'),
    'publication_year': pd.Series(dtype='int'),
    'total_copies': pd.Series(dtype='int')
})
data = [[1, 1, 'Alice Smith', '2024-01-15', None], [2, 1, 'Bob Johnson', '2024-01-20', None], [3, 2, 'Carol White', '2024-01-10', '2024-01-25'], [4, 3, 'David Brown', '2024-02-01', None], [5, 4, 'Emma Wilson', '2024-01-05', None], [6, 5, 'Frank Davis', '2024-01-18', '2024-02-10'], [7, 1, 'Grace Miller', '2024-02-05', None], [8, 6, 'Henry Taylor', '2024-01-12', None], [9, 2, 'Ivan Clark', '2024-02-12', None], [10, 2, 'Jane Adams', '2024-02-15', None]]
borrowing_records = pd.DataFrame({
    'record_id': pd.Series(dtype='int'),
    'book_id': pd.Series(dtype='int'),
    'borrower_name': pd.Series(dtype='str'),
    'borrow_date': pd.Series(dtype='datetime64[ns]'),
    'return_date': pd.Series(dtype='datetime64[ns]')
})
'''

import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    book_id_map = defaultdict(int)

    for i, r in borrowing_records.iterrows():
        if pd.isna(r['return_date']):
            book_id_map[r['book_id']] += 1

    df = library_books[library_books['book_id'].isin(book_id_map.keys())]
    df = df[df['total_copies'] == df['book_id'].map(book_id_map)]
    df = df.rename(columns={'total_copies': 'current_borrowers'})
    df = df.sort_values(by=['current_borrowers', 'title'], ascending=[False, True])
    return df
