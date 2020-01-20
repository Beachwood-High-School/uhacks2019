from __future__ import print_function
import sys
import csv
import requests
from bs4 import BeautifulSoup
from crawl import *
from multiprocessing import Process,Manager,managers


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

runner = int(sys.argv[1])
#print(runner)
cite = []
avglen = 0
global done
done = 0

def get_single_item_data(item_url):
    tempcite = []
    try:
        source_code = requests.get(item_url[0], timeout=5)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="lxml")

        for item_name in soup.findAll('a', {'class': 'external text'}):

            ref = item_name.get('href')
            tempcite.append(fixext(ref))
        #print(item_url[0] + " " + str(len(tempcite))+ " " + str(10-done) + "/10")
    except Exception:
        pass
    return tempcite

def calcRange(pamrange):
    global done, cite
    for i in pamrange:
        cite.append(get_single_item_data(i))
        done+=1
    return cite

try:
    # pool = MP.Pool(processes=3)
    with open('example2.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, quoting=csv.QUOTE_ALL)
        global pamreader
        pamreader = list(spamreader)

    global spamlen
    spamlen = len(pamreader)
    cite = calcRange(pamreader[(runner*10):(((runner+1)*10))])


    myFile = open('runner/cite'+str(runner)+'.csv', 'w')
    with myFile:
        writer=csv.writer(myFile, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(cite)
    for row in cite:
        avglen += len(row)

    lencite = len(cite)
    #lencite = 2
    if lencite!=10:
        eprint('Average cites per article '+str(avglen/lencite)+' '+str(lencite)+' '+str(runner))
#else:
   # print('Average cites per article '+str(avglen/lencite)+' '+str(lencite)+' '+str(runner))
#print('Total cites ' + str(avglen))
except:
    print(str(runner)+' '+str(lencite))