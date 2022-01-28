import sqlite3

conn = sqlite3.connect('BurnerTemperatureDB.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE "BurnerTemp" (
    "TableID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    "Day" TEXT NOT NULL,
    "BurnerZone" INTEGER NOT NULL,
    "Burner" INTEGER NOT NULL,
    "Temperature" INTEGER NOT NULL)''')

print("Database created")