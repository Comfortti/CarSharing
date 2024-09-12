#Importing sqlite3 and connecting to the database
import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

cursor.execute('''
SELECT Timestamp, MAX(Demand) AS Max_Demand_2017
FROM CarSharing
WHERE Timestamp >= '2017-01-01' AND Timestamp < '2018-01-01'
''')

High_demand = cursor.fetchall()
print(High_demand)

connection.close() 