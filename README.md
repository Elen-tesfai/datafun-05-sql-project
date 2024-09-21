# datafun-05-sql

## Overview
This project integrates Python and SQL, focusing on database interactions using SQLite. It introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

## Project Description
Note: We're back to modules for this project. I recommend it for practice. We'll return to Jupyter again later.

We'll use Python to create and manage the overall database. 
We'll use SQL to interact with the relational data and tables. 
Our DBMS is SQLite, a lightweight, file-based database widely used in browsers, mobile devices, and more. 
We might use several packages from the Python Standard Library:
- `csv` - optional - I personally prefer using pandas as the code is a bit cleaner
- `pathlib`
- `sqlite3`
- `uuid` - optional - utility for creating unique ids (helpful with databases)

We'll also add an external dependency (e.g. pandas), so we'll need to create a project-specific virtual environment using venv and pip. 
- `pandas` to read from CSV with cleaner code
- `pyarrow` (as pandas requires the installation of pyarrow to work)

## Import Dependencies
```python
import pandas
import pyarrow  # required when using pandas
import numpy
import scipy
import seaborn
import matplotlib