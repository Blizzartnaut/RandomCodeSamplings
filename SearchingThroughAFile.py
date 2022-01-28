import re
cont = False
while cont == False:
    try:
        filename = input("What file do you want to open? ")
        filehandler = open(filename)
        cont = True
    except:
        print(str(filename) + " cannot be reached, or opened.")
        print("Please try again")
"""    
didyoudoit = False
splitit = input("Do you want to split the information? y/n >")
if splitit == "y":
    delim = input("What do you want to use as a delimiter?" + f"\n" + "WoA . or , for sentence structured documents. >")
    for line in filehandler:
        filecontents = line.split(delim)
    didyoudoit = True
    splitit = input("Do you want to use another delimiter? y/n >")"""

search1 = input("What are you looking for? ")
found = False
for line in filehandler:
    if re.search(search1, line):
        line = line.strip()
        list1 = line
        print(line)
        found = True
        splitit = input("Do you want to split the information? y/n >")
        if splitit == "y":
            delim = input("What do you want to use as a delimiter? ")
            x = line
            x = line.split(str(delim))
            splitit = input("Do you want to use another delimiter? y/n >")
            print(x)
        if found == False:
            print("No line with that string was found")