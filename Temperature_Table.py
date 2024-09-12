#Importing sqlite3 and connecting to the database
import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

#create a backup table that is a replica of the CarSharing table
temp_table = '''
CREATE TABLE IF NOT EXISTS Temperature AS
SELECT Temp, Temp_Feel, Temp_Category 
FROM CarSharing
'''
cursor.execute(temp_table)
print('New Temperature Table Created')

#SQLite does not support dropping a column, therefore to circumnavigate this I need to:
#create a temporary backup table, but without the Temp and the Temp_Feel 
#insert all the original data into the temp backup table (minus the Temp and Temp_Feel)
#drop the original table 
#create a new table with the same name as the original table
#insert the data from the backup table into the new original table
#drop the temporary table 
#solution was inspired from https://stackoverflow.com/questions/8442147/how-to-delete-or-add-column-in-sqlite 
drop_temp = '''
    PRAGMA foreign_keys = off;
    BEGIN TRANSACTION;
    CREATE TEMPORARY TABLE CarSharing_Backup2(ID, Timestamp, Season, Holiday, WorkingDay, Weather, Humidity, WindSpeed, Demand, Temp_Category);
    INSERT INTO CarSharing_Backup2 SELECT ID, Timestamp, Season, Holiday, WorkingDay, Weather, Humidity, WindSpeed, Demand, Temp_Category FROM CarSharing;
    DROP TABLE CarSharing; 
    CREATE TABLE CarSharing (ID, Timestamp, Season, Holiday, WorkingDay, Weather, Humidity, WindSpeed, Demand, Temp_Category);
    INSERT INTO CarSharing SELECT ID, Timestamp, Season, Holiday, WorkingDay, Weather, Humidity, WindSpeed, Demand, Temp_Category FROM CarSharing_Backup2;
    DROP TABLE CarSharing_Backup2; 
    COMMIT;
    PRAGMA foreign_keys = on;
'''
cursor.executescript(drop_temp)
print('Columns "Temp" and "Temp_Feel" have been removed from the CarSharing table')

connection.close()