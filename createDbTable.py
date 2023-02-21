import psycopg2

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

#Closing the connection
conn.close()