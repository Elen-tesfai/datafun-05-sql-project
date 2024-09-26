# Import from Python Standard Library
import sqlite3
import pathlib
import pandas as pd

# Define paths using joinpath
db_file_path = pathlib.Path("project.db")
city_data_path = pathlib.Path("C:/Users/su_te/datafun-05-sql-project/data/city.csv")
country_data_path = pathlib.Path("C:/Users/su_te/datafun-05-sql-project/data/country.csv")
countrylanguage_data_path = pathlib.Path("C:/Users/su_te/datafun-05-sql-project/data/countrylanguage.csv")

def verify_and_create_folders(paths):
    """Verify and create folders if they don't exist."""
    for path in paths:
        folder = path.parent
        if not folder.exists():
            print(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
        else:
            print(f"Folder already exists: {folder}")

def create_database(db_path):
    """Create a new SQLite database file if it doesn't exist."""
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")

def create_tables(db_path):
    """Create necessary tables in the database."""
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS city (
                ID INTEGER PRIMARY KEY,
                Name TEXT,
                CountryCode TEXT,
                District TEXT,
                Population INTEGER
            )''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS country (
                CountryID INTEGER PRIMARY KEY,
                CountryCode TEXT,
                CountryName TEXT,
                Region TEXT
            )''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS countrylanguage (
                CountryID INTEGER,
                Language TEXT NOT NULL,
                IsOfficial BOOLEAN,
                Percentage DECIMAL,
                FOREIGN KEY (CountryID) REFERENCES country(CountryID)
            )''')

            print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def insert_data_from_csv(db_path):
    """Read data from CSV files and insert the records into their respective tables."""
    try:
        cities_df = pd.read_csv(city_data_path)
        countries_df = pd.read_csv(country_data_path)
        languages_df = pd.read_csv(countrylanguage_data_path)

        # Print DataFrames to verify data loading
        print("Cities DataFrame:")
        print(cities_df)
        print("Countries DataFrame:")
        print(countries_df)
        print("Languages DataFrame:")
        print(languages_df)

        with sqlite3.connect(db_path) as conn:
            cities_df.to_sql("city", conn, if_exists="replace", index=False)
            countries_df.to_sql("country", conn, if_exists="replace", index=False)
            languages_df.to_sql("countrylanguage", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")

def main():
    # Verify and create necessary folders
    paths_to_verify = [city_data_path, country_data_path, countrylanguage_data_path]
    verify_and_create_folders(paths_to_verify)

    # Create the database and tables, then insert data
    create_database(db_file_path)
    create_tables(db_file_path)
    insert_data_from_csv(db_file_path)

if __name__ == "__main__":
    main()