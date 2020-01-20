from collections import Counter
import tldextract
import csv
from os import listdir
#hello =0
domains = []
runners = listdir('runner')


for i in runners:
    with open('runner/'+str(i), newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for link in spamreader:
            for i in link:
                #hello +=1
                domains.append(tldextract.extract(i).domain)
                
            #print(hello)


count = Counter(domains)
orderedlist = count.most_common(len(count))
myFile = open('domainlist.csv', 'w')
with myFile:
    writer = csv.writer(myFile,quoting= csv.QUOTE_NONNUMERIC)
    writer.writerows(orderedlist)
