import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

#Will need 13 columns for: 
#Month, Average Demand, Modal Temperature Category, Modal Weather, Average Windspeed
#Maximum windspeed, minimum windspeed, average humidity, max humidity
#min humidity, Average Demand when the weather is hot
#average demand when the weather is mild 
#average demand when the weather is cold 

cursor.execute('''
SELECT 
    Time.Month AS Month,
               
    AVG(CarSharing.Demand) AS Average_Demand,
               
    (SELECT Temp_Category 
     FROM (
        SELECT Temp_Category, COUNT(*) AS Category_Count
        FROM CarSharing
        WHERE (SELECT Month FROM Time WHERE Timestamp = CarSharing.Timestamp) = (
        SELECT Month
        FROM (SELECT Month, AVG(Demand) AS Avg_Demand
            FROM CarSharing
            JOIN Time ON CarSharing.Timestamp = Time.Timestamp
            WHERE CarSharing.Timestamp >= '2017-01-01' AND CarSharing.Timestamp < '2018-01-01'
            GROUP BY Month
            ORDER BY Avg_Demand DESC
            LIMIT 1
            ) AS Highest_demand_Month)
        AND CarSharing.Timestamp >= '2017-01-01' AND CarSharing.Timestamp < '2018-01-01'
        GROUP BY Temp_Category
        ORDER BY Category_Count DESC
     ) AS Temp_Cat) AS Modal_Temperature_Category,
               
    (SELECT Weather.Weather
     FROM (
        SELECT Weather_Code, COUNT(*) AS Weather_Count
        FROM CarSharing
        WHERE CarSharing.Timestamp >= '2017-01-01' AND CarSharing.Timestamp < '2018-01-01'
        GROUP BY Weather_Code
        ORDER BY Weather_Count DESC
        LIMIT 1
     ) AS Weather_Code_Count
     JOIN Weather ON Weather_Code_Count.Weather_Code = Weather.Weather_Code
    ) AS Modal_Weather,
               
    AVG(NULLIF(CarSharing.WindSpeed,'')) AS Average_Windspeed,
    MAX(NULLIF(CarSharing.WindSpeed, '')) AS Maximum_Windspeed,
    MIN(NULLIF(CarSharing.WindSpeed,'')) AS Minimum_Windspeed,
    AVG(NULLIF(CarSharing.Humidity,'')) AS Average_Humidity,
    MAX(NULLIF(CarSharing.Humidity,'')) AS Maximum_Humidity,
    MIN(NULLIF(CarSharing.Humidity,'')) AS Minimum_Humidity,
    AVG(CASE WHEN CarSharing.Temp_Category = 'Hot' THEN CarSharing.Demand ELSE NULL END) AS Average_Demand_Hot,
    AVG(CASE WHEN CarSharing.Temp_Category = 'Mild' THEN CarSharing.Demand ELSE NULL END) AS Average_Demand_Mild,
    AVG(CASE WHEN CarSharing.Temp_Category = 'Cold' THEN CarSharing.Demand ELSE NULL END) AS Average_Demand_Cold
FROM 
    CarSharing
JOIN 
    Time ON CarSharing.Timestamp = Time.Timestamp
WHERE 
    CarSharing.Timestamp >= '2017-01-01' AND CarSharing.Timestamp < '2018-01-01' AND CarSharing.WindSpeed IS NOT NULL AND CarSharing.Humidity IS NOT NULL
GROUP BY 
    Time.Month
ORDER BY 
    Average_Demand DESC
LIMIT 1; 
''')

HighDemandInfo = cursor.fetchall()
print(HighDemandInfo)

connection.close() 