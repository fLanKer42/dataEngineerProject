import openpyxl
 
# Define variable to load the dataframe
dataframe = openpyxl.load_workbook("test.xlsx")
 
# Define variable to read sheet
dataframe1 = dataframe.active

count = 0
# Iterate the loop to read the cell values
sheetData = list()
for row in range(4, dataframe1.max_row - 2):
    c = 0
    data = dict()
    for col in dataframe1.iter_cols(2, dataframe1.max_column):
        #print(col[row].value, end=" : ")
        if (c == 1):
            data["BANK NAME"] = col[row].value
        elif (c == 2):
            data["TOTAL OUTWARD DEBITS :: NO. OF OUTWARD TRANSACTIONS"] = col[row].value
        elif (c == 3):
            data["TOTAL OUTWARD DEBITS :: AMOUNT (LAKHS)"] = col[row].value
        elif (c == 4):
            data["RECIEVED INWARD CREDITS :: NO. OF INWARD TRANSACTIONS"] = col[row].value
        elif (c == 5):
            data["RECIEVED INWARD CREDITS :: AMOUNT (LAKHS)"] = col[row].value
        c+=1
    #print(" ")
    sheetData.append(data)
count = 0
for row in sheetData:
    if count > 10:
        break
    count+=1
    for key in row:
        print(key + " : " + str(row[key]))
