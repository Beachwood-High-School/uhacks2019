

import requests
from bs4 import BeautifulSoup

cite = []



def spider(url):
    
    if str(url[:24]) != 'https://en.wikipedia.org':
        url = 'https://en.wikipedia.org'+url
    get_single_item_data(url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="lxml")
    for link in soup.findAll('a', {'class': ''}):
        intlinks = []
        href = str(link.get('href'))
        print(href)
        if href[:6] == '/wiki/':
            # print('yes')
            intlinks.append(href)


def get_single_item_data(item_url):
    # print('called')
    if item_url[:4] != 'http':
        item_url = 'http:'+item_url
    source_code = requests.get(item_url, timeout=5)
    # print('got')
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="lxml")
    print(item_url)
    for item_name in soup.findAll('a', {'class': 'external text'}):
        item_name = str(item_name)
        if item_name[:4] == 'http':
            ref = item_name.get('href')
            cite.append(ref)

spider('https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/1')
print('hello')


myredos = 2

    