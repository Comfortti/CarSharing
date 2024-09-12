import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

cursor.execute('''
SELECT AVG(Demand) AS Average_Demand 
FROM CarSharing
WHERE CarSharing.Timestamp >= '2017-01-01' AND CarSharing.Timestamp < '2018-01-01'
''')

AVG_demand = cursor.fetchall()
print('The Average Demand in 2017 was:', AVG_demand)

connection.close() 