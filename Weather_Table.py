#Importing sqlite3 and connecting to the database
import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

#create a backup table that is a replica of the CarSharing table
weather_table = '''
CREATE TABLE IF NOT EXISTS Weather AS
SELECT Weather, Weather_Code
FROM CarSharing
'''
cursor.execute(weather_table)
print('New Weather Table Created')

#SQLite does not support dropping a column, therefore to circumnavigate this I need to:
#create a temporary backup table, but without the weather column
#insert all the original data into the temp backup table (minus the weather column)
#drop the original table 
#create a new table with the same name as the original table
#insert the data from the backup table into the new original table
#drop the temporary table 
#solution was inspired from https://stackoverflow.com/questions/8442147/how-to-delete-or-add-column-in-sqlite 
drop_weath = '''
    PRAGMA foreign_keys = off;
    BEGIN TRANSACTION;
    CREATE TEMPORARY TABLE CarSharing_Backup3(ID, Timestamp, Season, Holiday, WorkingDay, Humidity, WindSpeed, Demand, Temp_Category, Weather_Code);
    INSERT INTO CarSharing_Backup3 SELECT ID, Timestamp, Season, Holiday, WorkingDay, Humidity, WindSpeed, Demand, Temp_Category, Weather_Code FROM CarSharing;
    DROP TABLE CarSharing; 
    CREATE TABLE CarSharing (ID, Timestamp, Season, Holiday, WorkingDay, Humidity, WindSpeed, Demand, Temp_Category, Weather_Code);
    INSERT INTO CarSharing SELECT ID, Timestamp, Season, Holiday, WorkingDay, Humidity, WindSpeed, Demand, Temp_Category, Weather_Code FROM CarSharing_Backup3;
    DROP TABLE CarSharing_Backup3; 
    COMMIT;
    PRAGMA foreign_keys = on;
'''
cursor.executescript(drop_weath)
print('Column "Weather" has been removed from the CarSharing table')

connection.close()