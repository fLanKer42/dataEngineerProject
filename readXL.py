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
    data = list()
    data.append("2023")
    data.append("JAN")
    for col in dataframe1.iter_cols(2, dataframe1.max_column):
        #print(col[row].value, end=" : ")
        data.append(col[row].value)
    #print(" ")
    sheetData.append(data)
