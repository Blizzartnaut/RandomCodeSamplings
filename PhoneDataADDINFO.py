import sqlite3

conn = sqlite3.connect('BurnerTemperatureDB.sqlite')
cur = conn.cursor()

d = False
while d == False:
    try:
        day = input("What day is today? Please use month/day/year format ")
        d = True
    except:
        print("Information must be wrong.")

i = False
while i == False:
    try:
        deckwat = int(input("What deck are you shooting? "))
        i = True
    except:
        print("The deck has to be a whole number")

bzburn = {}
def deckread():
    bz= 1
    while bz < 13:
        temp = int(input("What Temperature did you record for Burner " + str(bz) + " "))
        bzburn[bz] = temp
        bz = bz + 1

deckread()
print(bzburn)

z = 1
while z < 13:
    try:
        cur.execute('''INSERT INTO BurnerTemp (Day, BurnerZone, Burner, Temperature) VALUES (?, ?, ?, ?)''', (day, deckwat, z, bzburn[z]))
        z = z + 1
    except:
        print("Something went wrong")
conn.commit()
conn.close()
print("Task carried out succesfully")