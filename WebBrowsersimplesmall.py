import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
loca=input("What page would you like to open? Please use full address >")
try:
    fhand = urllib.request.urlopen(loca).read()
except:
    print("Error 404")
    quit()
else:
    counts=dict()
    for line in fhand:
        words=line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    soup = BeautifulSoup(fhand, 'html.parser')
    ask=input("What would you like to do with this file? type histogram or search >")
    ask=ask.lower()
    numlist=list()

    if ask == 'search':
        search=input("What would you like to search for? ")
        for line in fhand:
            line=line.rstrip('<b>','</b>')
            stuff=re.findall(f'.*{search}.*', line)
            if stuff == None :
                continue
            print(str(stuff))
            #num = string(stuff[0])
            #numlist.append(num)
            #if len(numlist < 1):
            #    print('Maximum:', max(numlist))

    elif ask == 'histogram':
        lst = list()
        for key, val in counts.items():
            newtup=(val,key)
            lst.append(newtup)
        lst=sorted(lst, reverse=True)
        for val,key in lst[:20]:
            print(key,val)

    else:
        print("Invalid response")