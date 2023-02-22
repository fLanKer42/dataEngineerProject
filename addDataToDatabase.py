import psycopg2

def addRtgsDataToPostgresFromGivenDictionary(dict1):
    '''
    Add RTGS data to postgres database from given dictionary
    '''
    # Connect to database
    #establishing the connection
    conn = psycopg2.connect(
        database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Inserting records into table
    for key, value in dict1.items():
        sql = '''INSERT INTO RTGS(YEAR, MONTH, PARTICPANT, INWARD_VOLUME_INTERBANK, INWARD_VOLUME_CUSTOMER, INWARD_VOLUME_TOTAL, INWARD_VOLUME_PERCENT, INWARD_VALUE_INTERBANK_IN_CRORES, INWARD_VALUE_CUSTOMER_IN_CRORES, INWARD_VALUE_TOTAL_IN_CRORES, INWARD_VALUE_PERCENT, OUTWARD_VOLUME_INTERBANK, OUTWARD_VOLUME_CUSTOMER, OUTWARD_VOLUME_TOTAL, OUTWARD_VOLUME_PERCENT, OUTWARD_VALUE_INTERBANK_IN_CRORES, OUTWARD_VALUE_CUSTOMER_IN_CRORES, OUTWARD_VALUE_TOTAL_IN_CRORES, OUTWARD_VALUE_PERCENT) VALUES ('%s', '%s', '%s', %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        cursor.execute(sql, value)
        print("Record inserted")
    
    #Closing the connection
    conn.close()

def addNeftDataToPostgresFromGivenDictionary(dict1):
    '''
    Add NEFT data to postgres database from given dictionary
    '''
    # Connect to database
    #establishing the connection
    conn = psycopg2.connect(
        database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Inserting records into table
    for key, value in dict1.items():
        sql = '''INSERT INTO NEFT(YEAR, MONTH, BANK_NAME, NO_OF_OUTWARD_TRANSACTIONS, TOTAL_OUTWARD_DEBITS_AMOUNT_IN_LAKHS, NO_OF_INWARD_TRANSACTIONS, TOTAL_INWARD_CREDITS_AMOUNT_IN_LAKHS) VALUES ('%s', '%s', '%s', %s, %s, %s, %s)'''
        cursor.execute(sql, value)
        print("Record inserted")

    #Closing the connection
    conn.close()

if __name__ == '__main__':
    #dict1 = {'1': ('2019', 'January', 'Bank of Baroda', 0, 0.00, 0, 0.00), '2': ('2019', 'January', 'Bank of India', 0, 0.00, 0, 0.00), '3': ('2019', 'January', 'Bank of Maharashtra', 0, 0.00, 0, 0.00), '4': ('2019', 'January', 'Canara Bank', 0, 0.00, 0, 0.00), '5': ('2019', 'January', 'Central Bank of India', 0, 0.00, 0, 0.00), '6': ('2019', 'January', 'Corporation Bank', 0, 0.00, 0, 0.00), '7': ('2019', 'January', 'Dena Bank', 0, 0.00, 0, 0.00), '8': ('2019', 'January', 'Indian Bank', 0, 0.00, 0, 0.00), '9': ('2019', 'January', 'Indian Overseas Bank', 0, 0.00, 0, 0.00), '10': ('2019', 'January', 'Oriental Bank of Commerce', 0, 0.00, 0, 0.00), '11': ('2019', 'January', 'Punjab National Bank', 0, 0.00, 0, 0.00), '12': ('2019', 'January', 'State Bank of India', 0, 0.00, 0, 0.00), '13': ('2019', 'January', 'Syndicate Bank', 0, 0.00, 0, 0.00), '14': ('2019', 'January', 'UCO Bank', 0, 0.00, 0, 0.00), '15': ('2019', 'January', 'Union Bank of India', 0, 0.00, 0, 0.00)}
    #addDataToPostgresFromGivenDictionary(dict1)
    pass
