from bs4 import BeautifulSoup
import requests
import re


def fetch_links(dls):
    while(True):
        html_page = requests.get(dls)
        if (html_page.status_code == 200):
            print("Connection successful")
            break
        else:
            print("Connection failed")
            continue
    soup = BeautifulSoup(html_page.content, "html.parser")

    links = list()
    for link in soup.findAll('a'):
        x = re.search('.XLSX$', str(link.get('href')))
        if(x is not None):
            links.append(link.get('href'))
    return(links)

if __name__ == '__main__':
    dls = "https://rbi.org.in/Scripts/NEFTView.aspx"
    fetch_links(dls)