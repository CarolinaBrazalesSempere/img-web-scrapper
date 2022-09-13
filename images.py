import requests
import sys
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


input = sys.argv[1]
HTMLdata = getdata(input)
soup = BeautifulSoup(HTMLdata, 'html.parser')
images = soup.find_all('img')

for item in images:
    url = item['src']
    filename = url.split('/')[-1]
    with open("images\\" + filename, 'wb') as handler:
        handler.write(requests.get(url).content)
