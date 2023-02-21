import openpyxl

def read_XL():
    '''
    This function reads the excel file and returns the data in a dictionary
    '''
    # Define variable to load the dataframe
    dataframe = openpyxl.load_workbook("test.xlsx")

    dataframe1 = dataframe.active

    # Iterate the loop to read the cell values
    sheet_data = dict()

    count = 1
    for row in range(4, dataframe1.max_row - 2):
        data = list()
        data.append("2023")
        data.append("JAN")
        for col in dataframe1.iter_cols(2, dataframe1.max_column):
            #print(col[row].value, end=" : ")
            data.append(col[row].value)
        #print(" ")
        sheet_data[str(count)] = tuple(data)
        count += 1
    return sheet_data

if __name__ == '__main__':
    pass