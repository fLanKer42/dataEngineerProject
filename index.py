from fetch import fetch_url
from readXL import read_XL
from deleteXL import delete_XL
from createDatabaseTable import createDatabaseTable
from addDataToDatabase import addDataToPostgresFromGivenDictionary
from fetchLinksToExcelsFromRbi import fetch_url

# URL to download
#dls = ["https://rbidocs.rbi.org.in/rdocs/NEFT/DOCs/NEFTRTGSJAN20238F691C3E20284DB9827EE56F372B87C0.XLSX", "https://rbidocs.rbi.org.in/rdocs/NEFT/DOCs/NEFTRTGS12202212C659F93C5D4650BB3080583E8E5632.XLSX", "https://rbidocs.rbi.org.in/rdocs/NEFT/DOCs/NEFTRRTGS11202260E56A42B4834C548AC04863EA035FA8.XLSX"]

# Create the database table
createDatabaseTable()

dls = "https://rbi.org.in/Scripts/NEFTView.aspx"

dls = fetch_url(dls)

# Fetch the URL
for d in dls:
    fetch_url(d)
    sheet_data = read_XL()
    delete_XL()
    addDataToPostgresFromGivenDictionary(sheet_data)



