#Importing sqlite3 and connecting to the database
import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

cursor.execute('''
SELECT Weather_Code AS Modal_Weather_2017, COUNT(*) AS Category_Count
FROM CarSharing
WHERE Timestamp >= '2017-01-01' AND Timestamp < '2018-01-01'
GROUP BY Weather_Code
ORDER BY Category_Count DESC
LIMIT 1;
''')

ModalWeath = cursor.fetchall()
print(ModalWeath)

connection.close() 