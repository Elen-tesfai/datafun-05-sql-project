# SQLite Experiments

## Countries Table

**Query:**
```sql
SELECT * FROM country;
Results:

ID	Code	Name	Continent
1	US	United States	North America
2	CA	Canada	North America
3	GB	United Kingdom	Europe
4	FR	France	Europe
5	DE	Germany	Europe
6	JP	Japan	Asia
7	AU	Australia	Oceania
8	MX	Mexico	North America
9	CN	China	Asia
10	IN	India	Asia
Cities Table
Query:

sql
Copy code
SELECT * FROM city;
Results:

ID	City	Country Code	District	Population
1	CityA	US	DistrictA	500000
2	CityB	US	DistrictB	300000
3	CityC	CA	DistrictC	250000
4	CityD	US	DistrictD	700000
5	CityE	CA	DistrictE	400000
6	CityF	GB	DistrictF	350000
7	CityG	FR	DistrictG	600000
8	CityH	DE	DistrictH	450000
9	CityI	JP	DistrictI	800000
10	CityJ	AU	DistrictJ	550000
Country Languages Table
Query:

sql
Copy code
SELECT * FROM countrylanguage;
Results:

ID	Language	Country ID	Percentage
1	English	1	80.0
1	Spanish	1	15.0
1	French	1	5.0
2	English	2	60.0
2	French	2	40.0
3	English	3	80.0
3	Welsh	3	20.0
4	French	4	100.0
5	German	5	95.0
5	Turkish	5	5.0
6	Japanese	6	100.0
7	English	7	70.0
8	Spanish	8	90.0
9	Chinese	9	100.0
10	Hindi	10	50.0
10	English	10	30.0
