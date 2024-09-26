-- Query to select all countries
SELECT * FROM country;

-- Query to join cities with their respective countries
SELECT city.CityName, country.CountryName 
FROM city 
JOIN country ON city.CountryID = country.CountryID;

-- Query to find official languages and their percentages
SELECT country.CountryName, countrylanguage.Language, countrylanguage.Percentage 
FROM countrylanguage 
JOIN country ON countrylanguage.CountryID = country.CountryID 
WHERE countrylanguage.IsOfficial = TRUE;