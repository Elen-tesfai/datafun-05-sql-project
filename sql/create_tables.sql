-- Start by deleting any tables if they exist already
-- We want to be able to re-run this script as needed.
-- DROP tables in reverse order of creation 
-- DROP dependent tables (with foreign keys) first

DROP TABLE IF EXISTS countrylanguage;
DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS country;

-- Create the country table 
-- Note that the country table has no foreign keys, so it is a standalone table
CREATE TABLE country (
    CountryID INTEGER PRIMARY KEY,
    CountryName TEXT NOT NULL,
    CountryCode TEXT UNIQUE NOT NULL
);

-- Create the city table
-- Note that the city table has a foreign key to the country table
-- This means that the city table is dependent on the country table
-- Be sure to create the standalone country table BEFORE creating the city table.
CREATE TABLE city (
    CityID INTEGER PRIMARY KEY,
    CityName TEXT NOT NULL,
    CountryID INTEGER,
    FOREIGN KEY (CountryID) REFERENCES country(CountryID)
);

-- Create the countrylanguage table
-- The countrylanguage table has a foreign key to the country table
-- This means that the countrylanguage table is dependent on the country table
CREATE TABLE countrylanguage (
    CountryID INTEGER,
    Language TEXT NOT NULL,
    IsOfficial BOOLEAN,
    Percentage DECIMAL,
    FOREIGN KEY (CountryID) REFERENCES country(CountryID)
);