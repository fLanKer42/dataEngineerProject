# Fetches data from RBI website and stores it in a postgres database

## Usage
run ```python index.py``` in the terminal

## Working
The scripts are written in Python 3.6. The data is fetched from the RBI website and stored in a PostgreSQL database. The scripts are written in such a way that they can be used to fetch data from the website and store it in the Postgres database.
The database has two tables: NEFT and RTGS. The NEFT table stores data about the NEFT transactions and the RTGS table stores data about the RTGS transactions.

## Directory Structure
```
.
├── README.md
├── createDatabaseTable.py
├── fetchLinksToExcelsFromRbi.py
├── fetch.py
├── index.py
├── readXL.py
├── deleteXL.py
└── addDataToDatabase.py
```

## Scripts

### index.py
Acts as a wrapper for the other scripts. It calls the other scripts in the order in which they are called.

### index.py calls the following scripts in the following order:
1. createDatabaseTable.py
2. fetchLinksToExcelsFromRbi.py
3. fetch.py
4. readXL.py
5. deleteXL.py
6. addDataToDatabase.py

### createDatabaseTable.py
Creates a table in the database

### fetchLinksToExcelsFromRbi.py
Fetches the links to the .xlsx files from RBI website

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
6. bs4
7. re
8. os

## Database
1. Database name: rbi
2. Table name: NEFT
3. Columns: YEAR, MONTH, BANK_NAME, NO_OF_OUTWARD_TRANSACTIONS, TOTAL_OUTWARD_DEBITS_AMOUNT_IN_LAKHS, NO_OF_INWARD_TRANSACTIONS, TOTAL_INWARD_CREDITS_AMOUNT_IN_LAKHS
4. Table name: RTGS
5. Columns: YEAR, MONTH, PARTICPANT, INWARD_VOLUME_INTERBANK, INWARD_VOLUME_CUSTOMER, INWARD_VOLUME_TOTAL, INWARD_VOLUME_PERCENT, INWARD_VALUE_INTERBANK_IN_CRORES, INWARD_VALUE_CUSTOMER_IN_CRORES, INWARD_VALUE_TOTAL_IN_CRORES, INWARD_VALUE_PERCENT, OUTWARD_VOLUME_INTERBANK, OUTWARD_VOLUME_CUSTOMER, OUTWARD_VOLUME_TOTAL, OUTWARD_VOLUME_PERCENT, OUTWARD_VALUE_INTERBANK_IN_CRORES, OUTWARD_VALUE_CUSTOMER_IN_CRORES, OUTWARD_VALUE_TOTAL_IN_CRORES, OUTWARD_VALUE_PERCENT

## Author
1. Name: Dhruv Rai
2. Email: dhruv.rai2001@gmail.com
3. Github: fLanKer42
