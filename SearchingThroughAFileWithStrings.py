filename = input("What file do you want to open? ")
try:
    filehandler = open(filename)
except:
    print(str(filename) + " cannot be reached, or opened.")
    quit()

var = input("What are you searching for? ")
found = False
for line in filehandler:
    if line.startswith(var):
        line = line.strip()
        print(line)
        found = True
if found == False:
    print("No line starting with that string was found")