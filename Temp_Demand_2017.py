import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

#in the table, there are empty strings which do not register as NULL
#so query converts them to NULL in order to not include
#the empty string in calculations 
#inspired from https://www.w3schools.com/sql/func_sqlserver_nullif.asp
cursor.execute('''
SELECT Temp_Category, AVG(NULLIF(Demand, '')) AS Average_Demand
FROM CarSharing
WHERE CarSharing.Timestamp >= '2017-01-01' AND CarSharing.Timestamp < '2018-01-01' AND CarSharing.WindSpeed IS NOT NULL
GROUP BY Temp_Category
ORDER BY Average_Demand DESC; 
''')

Demand = cursor.fetchall()
print(Demand)

connection.close() 