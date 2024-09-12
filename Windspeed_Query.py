import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

#in the table, there are empty strings which do not register as NULL
#so query converts them to NULL in order to not include
#the empty string in calculations 
#inspired from https://www.w3schools.com/sql/func_sqlserver_nullif.asp
cursor.execute('''
SELECT Time.Month, AVG(NULLIF(CarSharing.WindSpeed, '')) AS Average_Windspeed, MIN(NULLIF(CarSharing.Windspeed, '')) AS Lowest_Windspeed, MAX(NULLIF(CarSharing.WindSpeed, '')) AS Highest_Windspeed
FROM Time
INNER JOIN CarSharing ON Time.Timestamp = CarSharing.Timestamp
WHERE CarSharing.Timestamp >= '2017-01-01' AND CarSharing.Timestamp < '2018-01-01' AND CarSharing.WindSpeed IS NOT NULL
GROUP BY Time.Month
ORDER BY Average_Windspeed DESC; 
''')

WindSpeed = cursor.fetchall()
print(WindSpeed)

connection.close() 