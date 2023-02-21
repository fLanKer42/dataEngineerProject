import psycopg2

def addDataToPostgresFromGivenDictionary(dict1):
    '''Add data to postgres database from given dictionary'''
    # Connect to database
    #establishing the connection
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    sql = '''CREATE database mydb''';

    #Creating a database
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS NEFT")

    #Creating table as per requirement
    sql ='''CREATE TABLE NEFT(
    YEAR VARCHAR(4) NOT NULL,
    MONTH CHAR(10) NOT NULL,
    BANK_NAME CHAR(30) NOT NULL,
    NO_OF_OUTWARD_TRANSACTIONS INT,
    TOTAL_OUTWARD_DEBITS_AMOUNT_IN_LAKHS DECIMAL(12,2),
    NO_OF_INWARD_TRANSACTIONS INT,
    TOTAL_INWARD_CREDITS_AMOUNT_IN_LAKHS DECIMAL(12,2)
    )'''
    cursor.execute(sql)
    print("Table created successfully........")

    #Inserting records into table
    for key, value in dict1.items():
        sql = '''INSERT INTO NEFT(YEAR, MONTH, BANK_NAME, NO_OF_OUTWARD_TRANSACTIONS, TOTAL_OUTWARD_DEBITS_AMOUNT_IN_LAKHS, NO_OF_INWARD_TRANSACTIONS, TOTAL_INWARD_CREDITS_AMOUNT_IN_LAKHS) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        cursor.execute(sql, value)
        print("Record inserted")

    #Closing the connection
    conn.close()

if __name__ == '__main__':
    dict1 = {'1': ('2019', 'January', 'Bank of Baroda', 0, 0.00, 0, 0.00), '2': ('2019', 'January', 'Bank of India', 0, 0.00, 0, 0.00), '3': ('2019', 'January', 'Bank of Maharashtra', 0, 0.00, 0, 0.00), '4': ('2019', 'January', 'Canara Bank', 0, 0.00, 0, 0.00), '5': ('2019', 'January', 'Central Bank of India', 0, 0.00, 0, 0.00), '6': ('2019', 'January', 'Corporation Bank', 0, 0.00, 0, 0.00), '7': ('2019', 'January', 'Dena Bank', 0, 0.00, 0, 0.00), '8': ('2019', 'January', 'Indian Bank', 0, 0.00, 0, 0.00), '9': ('2019', 'January', 'Indian Overseas Bank', 0, 0.00, 0, 0.00), '10': ('2019', 'January', 'Oriental Bank of Commerce', 0, 0.00, 0, 0.00), '11': ('2019', 'January', 'Punjab National Bank', 0, 0.00, 0, 0.00), '12': ('2019', 'January', 'State Bank of India', 0, 0.00, 0, 0.00), '13': ('2019', 'January', 'Syndicate Bank', 0, 0.00, 0, 0.00), '14': ('2019', 'January', 'UCO Bank', 0, 0.00, 0, 0.00), '15': ('2019', 'January', 'Union Bank of India', 0, 0.00, 0, 0.00)}
    addDataToPostgresFromGivenDictionary(dict1)
