import csv
import sqlite3  # or your preferred database module

# Connect to your database (create it if it doesn't exist)
conn = sqlite3.connect('book_db.sqlite')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS authors (
    author_id TEXT PRIMARY KEY,
    first TEXT,
    last TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY(author_id) REFERENCES authors(author_id)
)
''')

# Clear existing data
cursor.execute("DELETE FROM authors")
cursor.execute("DELETE FROM books")

# Read authors
with open('C:/Users/su_te/datafun-05-sql/data/authors.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''
            INSERT INTO authors (author_id, first, last)
            VALUES (?, ?, ?)
        ''', (row['author_id'], row['first'], row['last']))

# Read books
with open('C:/Users/su_te/datafun-05-sql/data/books.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''
            INSERT INTO books (book_id, title, year_published, author_id)
            VALUES (?, ?, ?, ?)
        ''', (row['book_id'], row['title'], row['year_published'], row['author_id']))

# Commit changes and close the connection
conn.commit()
conn.close()