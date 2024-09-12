#Importing sqlite3 and connecting to the database
import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

#create the table for the csv file to be imported into 
sql = '''
CREATE TABLE CarSharing(
    ID INTEGER PRIMARY KEY,
    Timestamp TEXT, 
    Season TEXT,
    Holiday TEXT,
    WorkingDay TEXT,
    Weather TEXT,
    Temp REAL,
    Temp_Feel REAL,
    Humidity REAL,
    WindSpeed REAL,
    Demand REAL
    ) '''

cursor.execute(sql)
print("Database created successfully")

#insert the csv records into the CarSharing table 
with open('CarSharing.csv', 'r') as file:
    records = 0 
    next(file)
    for row in file: 
        cursor.execute('INSERT INTO CarSharing VALUES (?,?,?,?,?,?,?,?,?,?,?)', row.split(','))
        records += 1
print("\n{} records successfully imported into CarSharing table".format(records))

#create a backup table that is a replica of the CarSharing table
backup = '''
CREATE TABLE IF NOT EXISTS CarSharing_Backup AS
SELECT * FROM CarSharing WHERE 1=0
'''
cursor.execute(backup)

#insert the same records from the main CarSharing table, into the backup table
insert2backup = 'INSERT INTO CarSharing_Backup SELECT * FROM CarSharing'
cursor.execute(insert2backup)
print("\n{} records successfully imported into CarSharing_Backup table".format(records))

connection.close()