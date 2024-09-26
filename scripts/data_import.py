import csv
import sqlite3
import pathlib

# Define paths
db_file_path = pathlib.Path("C:/Users/su_te/datafun-05-sql-project/data/book_db.sqlite")
city_data_path = pathlib.Path("C:/Users/su_te/datafun-05-sql-project/data/city.csv")
country_data_path = pathlib.Path("C:/Users/su_te/datafun-05-sql-project/data/country.csv")
countrylanguage_data_path = pathlib.Path("C:/Users/su_te/datafun-05-sql-project/data/countrylanguage.csv")

# Connect to your database (create it if it doesn't exist)
conn = sqlite3.connect(db_file_path)
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
try:
    with open(country_data_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
                INSERT INTO authors (author_id, first, last)
                VALUES (?, ?, ?)
            ''', (row['author_id'], row['first'], row['last']))
    print("Authors data inserted successfully.")
except Exception as e:
    print(f"Error reading authors data: {e}")

# Read books
try:
    with open(city_data_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
                INSERT INTO books (book_id, title, year_published, author_id)
                VALUES (?, ?, ?, ?)
            ''', (row['book_id'], row['title'], row['year_published'], row['author_id']))
    print("Books data inserted successfully.")
except Exception as e:
    print(f"Error reading books data: {e}")

# Commit changes and close the connection
conn.commit()
conn.close()