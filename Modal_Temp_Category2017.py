#Importing sqlite3 and connecting to the database
import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

cursor.execute('''
SELECT Temp_Category AS Modal_Temp_Cat_2017, COUNT(*) AS Category_Count
FROM CarSharing
WHERE Timestamp >= '2017-01-01' AND Timestamp < '2018-01-01'
GROUP BY Temp_Category
ORDER BY Category_Count DESC
LIMIT 1;
''')

ModalTempCat = cursor.fetchall()
print(ModalTempCat)

connection.close() 