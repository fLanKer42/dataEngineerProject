import requests
# URL to download


def fetch_url(dls):
    '''
    Fetches the URL and saves the file to the current directory
    '''
    resp = requests.get(dls, timeout=10)
    output = open('test.xlsx', 'wb')
    output.write(resp.content)
    output.close()

if __name__ == '__main__':
    dls = "https://rbidocs.rbi.org.in/rdocs/NEFT/DOCs/NEFTRTGSJAN20238F691C3E20284DB9827EE56F372B87C0.XLSX"
    fetch_url(dls)

