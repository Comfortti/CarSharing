#Importing sqlite3 and connecting to the database
import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

#cursor.execute('ALTER TABLE CarSharing ADD COLUMN Weather_Code INTEGER')

weather_code = '''
UPDATE CarSharing
SET Weather_Code = (
    SELECT COUNT(DISTINCT Weather)
    FROM CarSharing AS Car2
    WHERE Car2.Weather <= CarSharing.Weather
    )
'''
cursor.execute(weather_code)
print("New Weather Code Column has successfully been added and populated")

connection.close()