#Importing sqlite3 and connecting to the database
import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

cursor.execute('''
SELECT Time.Hour AS Monday_2017_Hours, AVG(CarSharing.Demand) AS Average_Demand
FROM Time
INNER JOIN CarSharing ON Time.Timestamp = CarSharing.Timestamp
WHERE CarSharing.Timestamp >= '2017-01-01' AND CarSharing.Timestamp < '2018-01-01' AND Time.Weekday = 'Monday'
GROUP BY Time.Hour 
ORDER BY Average_Demand DESC;
               ''')

Mon2017_demand = cursor.fetchall()
print(Mon2017_demand)

connection.close() 