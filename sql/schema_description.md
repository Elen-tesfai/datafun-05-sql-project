# Database Schema Description

## Tables

### Country
- **CountryID**: Primary key, unique identifier for each country.
- **CountryName**: Name of the country.
- **CountryCode**: Unique code for the country.

### City
- **CityID**: Primary key, unique identifier for each city.
- **CityName**: Name of the city.
- **CountryID**: Foreign key referencing CountryID in the Country table.

### CountryLanguage
- **CountryID**: Foreign key referencing CountryID in the Country table.
- **Language**: Language spoken in the country.
- **IsOfficial**: Boolean indicating if the language is official.
- **Percentage**: Percentage of the population speaking the language.