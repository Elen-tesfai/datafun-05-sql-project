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

## 1. Installation
To set up this project locally, follow these steps:

- Clone the repository:
    ```bash
    git clone https://github.com/Elen-tesfai/datafun-05-sql-project.git
    cd datafun-05-sql-project
    ```
- Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
- Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
## 2. Usage
To run the project, use the following commands:
```bash
python data_import.py
```
## 3. Project Structure
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
```
## 4. Backups
```
This project includes backup files located in the backups directory:
```
- authors_backup.csv: Backup of authors data.
- books_backup.csv: Backup of books data.
- Additional backups are organized in the data_backup folder.

### Screenshots
Below are screenshots showcasing key components of the project:

![alt text](<Screenshot%2024-09-26%20013104.png>)
![alt text](<Screenshot%2024-09-26%20013518.png>)

### Conclusion
In this project, we explored the integration of Python and SQL, enhancing our data management skills and gaining valuable insights from relational data.