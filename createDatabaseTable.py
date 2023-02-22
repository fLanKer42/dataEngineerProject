# Description: Create database and table
import psycopg2

def createDatabaseTable():
    '''
    Create database table
    '''
    # Connect to database
    #establishing the connection
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    sql = '''CREATE database rbi'''

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

    cursor.execute("DROP TABLE IF EXISTS RTGS")

    #Creating table as per requirement
    sql ='''CREATE TABLE RTGS(
    YEAR VARCHAR(4) NOT NULL,
    MONTH CHAR(10) NOT NULL,
    PARTICIPANT_NAME CHAR(30) NOT NULL,
    INWARD_VOLUME_INTERBANK INT,
    INWARD_VOLUME_CUSTOMER INT,
    INWARD_VOLUME_TOTAL INT,
    INWARD_VOLUME_PERCENT DECIMAL(12,2),
    OUTWARD_VOLUME_INTERBANK INT,
    OUTWARD_VOLUME_CUSTOMER INT,
    OUTWARD_VOLUME_TOTAL INT,
    OUTWARD_VOLUME_PERCENT DECIMAL(12,2),
    INWARD_VALUE_INTERBANK DECIMAL(12,2),
    INWARD_VALUE_CUSTOMER DECIMAL(12,2),
    INWARD_VALUE_TOTAL DECIMAL(12,2),
    INWARD_VALUE_PERCENT DECIMAL(12,2),
    OUTWARD_VALUE_INTERBANK DECIMAL(12,2),
    OUTWARD_VALUE_CUSTOMER DECIMAL(12,2),
    OUTWARD_VALUE_TOTAL DECIMAL(12,2),
    OUTWARD_VALUE_PERCENT DECIMAL(12,2)
    )'''
    cursor.execute(sql)

    print("Tables created successfully........")

    #Closing the connection
    conn.close()

if __name__ == '__main__':
    pass