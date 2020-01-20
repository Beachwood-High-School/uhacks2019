import sys
import requests
from bs4 import BeautifulSoup
import csv

level = 3 #don't mess with anything but this unless you want to mess with the code
# level 1=10pages,2=100,3=1000,4=10000,5=50000
#don't go above 3 if you're in the cloud and don't want to go broke

intlinks=[]
notallowed = [
    '/wiki/Main_Page',
    '/wiki/Main_Page'
]

def fix(url):
    if str(url[:24])!='https://en.wikipedia.org':
        url = 'https://wikipedia.org'+url
    elif str(url[:4])!='http':
        url = 'http'+url
    else:
        pass
    return url

def fixext(url):
    if str(url[:4])!='http':
        url = 'http:'+url
    else:
        pass
    return url

def spider(url):
    url = fix(url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,features="lxml")
    for link in soup.findAll('a',{'class':''}):
        href = str(link.get('href'))
        #print(href)
        if href[:6] == '/wiki/' and ':' not in href and href not in notallowed:
            '''or str(href[:24])!='https://en.wikipedia.org'''
            #print('yes')
            intlinks.append(str(fix(href)))
            



spider('https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/'+str(level))
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile, quoting=csv.QUOTE_ALL)
    for i in range(len(intlinks)):
       writer.writerow([intlinks[i]])
