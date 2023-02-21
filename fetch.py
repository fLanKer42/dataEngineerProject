import requests

def fetch_url(dls):
    '''
    Fetches the URL and saves the file to the current directory
    '''
    while(True):
        html_page = requests.get(dls)
        if (html_page.status_code == 200):
            print("Connection successful")
            break
        else:
            print("Connection failed")
            continue
    output = open('test.xlsx', 'wb')
    output.write(html_page.content)
    output.close()

if __name__ == '__main__':
    dls = "https://rbidocs.rbi.org.in/rdocs/NEFT/DOCs/NEFTRTGSJAN20238F691C3E20284DB9827EE56F372B87C0.XLSX"
    fetch_url(dls)

