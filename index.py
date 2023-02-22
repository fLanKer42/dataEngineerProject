# Description: This is the main file which will be executed to fetch the data from RBI website and store it in the database
from fetch import fetch_url
from readXL import read_neft_XL, read_rtgs_XL
from deleteXL import delete_XL
from createDatabaseTable import createDatabaseTable
from addDataToDatabase import addNeftDataToPostgresFromGivenDictionary, addRtgsDataToPostgresFromGivenDictionary
from fetchLinksToExcelsFromRbi import fetch_links

# Create the database table
createDatabaseTable()

URL = "https://rbi.org.in/Scripts/NEFTView.aspx"

DLS = fetch_links(URL)

# Fetch the URL
for d in DLS:
    fetch_url(d)
    neft_sheet_data = read_neft_XL()
    rtgs_sheet_data = read_rtgs_XL()
    delete_XL()
    addNeftDataToPostgresFromGivenDictionary(neft_sheet_data)
    addRtgsDataToPostgresFromGivenDictionary(rtgs_sheet_data)
