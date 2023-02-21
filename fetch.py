import requests
dls = "https://rbidocs.rbi.org.in/rdocs/NEFT/DOCs/NEFTRTGSJAN20238F691C3E20284DB9827EE56F372B87C0.XLSX"
resp = requests.get(dls)

output = open('test.xlsx', 'wb')
output.write(resp.content)
output.close()
