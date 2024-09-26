# datafun-05-sql-project

## Overview
This project integrates Python and SQL to work with well-structured relational data, demonstrating core competencies and skills associated with basic SQL.

## Project Description
In this project, we will:
- Utilize Python to manage and manipulate the database.
- Perform various SQL operations including queries, joins, filters, and aggregations.
- Leverage pandas for data manipulation and sqlite3 for database interactions.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Backups](#backups)
5. [Screenshots](#screenshots)
6. [Conclusion](#conclusion)

## Installation
To set up this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Elen-tesfai/datafun-05-sql-project.git
    cd datafun-05-sql-project
    ```
2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the project, use the following commands:
```bash
python data_import.py
```
## Project Structure
```

datafun-05-sql-project/
│
├── backups/
│   ├── data_backup/
│   ├── scripts_backup/
│   ├── sql_backup/
│   ├── book_manager_backup.py
│   └── project_backup.db 
│
├── data/
│   ├── city.csv
│   ├── country.csv
│   └── countrylanguage.csv
├── scripts/
│   └── data_import.py 
├── sql/
│   └── create_tables.sql
├── project.db 
├── README.md
├── requirements.txt
└── world_manager.py