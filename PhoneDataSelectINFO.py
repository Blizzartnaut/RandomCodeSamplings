import sqlite3

conn = sqlite3.connect('BurnerTemperatureDB.sqlite')
cur = conn.cursor()

var1 = input("What day do you want to look through >")
var2 = input("What BurnerZone? ")

cur.execute('''
SELECT BurnerZone, Burner, Temperature 
FROM BurnerTemp
Where Day=:var1 and BurnerZone=:var2
''', (var1, var2))

print("For day " + str(var1) + "and BurnerZone " + str(var2))
data = cur.fetchall()

for row in data:
    print("Burner", row[1], "Temp", row[2], end=", ")