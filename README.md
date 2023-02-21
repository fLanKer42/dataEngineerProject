# Fetches data from RBI website and stores it in a postgres database
index.py acts as a wrapper for the other scripts
### Usage: python index.py

### index.py calls the following scripts in the following order:
1. createDatabaseTable.py
2. fetch.py
3. readXL.py
4. deleteXL.py
5. addDataToDatabase.py

### createDatabaseTable.py
Creates a table in the database

### fetch.py
Fetches the data from RBI website and stores it in a .xlsx file

### readXL.py
Reads the .xlsx file and return a dictionary of tuples

### deleteXL.py
Deletes the .xlsx file

### addDataToDatabase.py
Adds the data to the database

## Dependencies
1. Python 3.6
2. PostgreSQL 9.6
3. psycopg2
4. requests
5. openpyxl

## Database
1. Database name: rbi
2. Table name: NEFT
3. Columns: YEAR, MONTH, BANK_NAME, NO_OF_OUTWARD_TRANSACTIONS, TOTAL_OUTWARD_DEBITS_AMOUNT_IN_LAKHS, NO_OF_INWARD_TRANSACTIONS, TOTAL_INWARD_CREDITS_AMOUNT_IN_LAKHS

## Author
1. Name: Dhruv Rai
2. Email: dhruv.rai2001@gmail.com
3. Github: fLanKer42
