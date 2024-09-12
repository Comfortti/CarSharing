#Importing sqlite3 and connecting to the database
import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

cursor.execute('''
WITH HighLowDemand AS (
    SELECT CarSharing.Timestamp, Time.Weekday, Time.Month, CarSharing.Season, CarSharing.Demand AS Demand, 
           COUNT(*) OVER (PARTITION BY Time.Weekday, Time.Month, CarSharing.Season) AS Count_Column
    FROM Time 
    INNER JOIN CarSharing ON Time.Timestamp = CarSharing.Timestamp
    WHERE Time.Timestamp >= '2017-01-01' AND Time.Timestamp < '2018-01-01' 
    AND CarSharing.Demand = (SELECT MAX(Demand) FROM CarSharing WHERE Timestamp >= '2017-01-01' AND Timestamp < '2018-01-01')
    GROUP BY CarSharing.Timestamp, Time.Weekday, Time.Month, CarSharing.Season

    UNION ALL

    SELECT CarSharing.Timestamp, Time.Weekday, Time.Month, CarSharing.Season, CarSharing.Demand AS Demand, 
           COUNT(*) OVER (PARTITION BY Time.Weekday, Time.Month, CarSharing.Season) AS Count_Column
    FROM Time 
    INNER JOIN CarSharing ON Time.Timestamp = CarSharing.Timestamp
    WHERE Time.Timestamp >= '2017-01-01' AND Time.Timestamp < '2018-01-01' 
    AND CarSharing.Demand = (SELECT MIN(Demand) FROM CarSharing WHERE Timestamp >= '2017-01-01' AND Timestamp < '2018-01-01')
    GROUP BY CarSharing.Timestamp, Time.Weekday, Time.Month, CarSharing.Season
)
SELECT * FROM HighLowDemand

''')

season_demand = cursor.fetchall()
print(season_demand)

connection.close() 