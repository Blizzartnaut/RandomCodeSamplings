import re
loca=input("What document would you like to open? Please use full address >")
try:
    fhand = open(loca)
except:
    print("Error 404")
    quit()
else:

    ask=input("What would you like to do with this file? type histogram or search >")
    ask=ask.lower()
    numlist=list()

    if ask == 'search':
        search=input("What would you like to search for? ")
        for line in fhand:
            stuff = None
            line=line.rstrip()
            stuff=re.findall(f'.*{search}.*\\s*', line)
            if stuff is None :
                continue
            print(str(stuff))
            #num = string(stuff[0])
            #numlist.append(num)
            #if len(numlist < 1):
            #    print('Maximum:', max(numlist))

    elif ask == 'histogram':
        counts=dict()
        for line in fhand:
            words=line.split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1
        lst = list()
        a = int(input("How many counts minimum for display? "))
        for key, val in counts.items():
            newtup=(val,key)
            lst.append(newtup)
        lst=sorted(lst, reverse=True)
        for val,key in lst[:a]:
            print(key,val)

    else:
        print("Invalid response")