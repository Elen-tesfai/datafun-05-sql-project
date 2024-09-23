-- Start by deleting any tables if they exist already
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

-- Create the authors table 
-- Note that the author table has no foreign keys, so it is a standalone table
CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    year_born INTEGER
);

-- Create the books table
-- Note that the books table has a foreign key to the authors table
CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);