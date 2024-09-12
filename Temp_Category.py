#Importing sqlite3 and connecting to the database
import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

#Add a a new column called Temp_Category 
cursor.execute('ALTER TABLE CarSharing ADD COLUMN Temp_Category VARCHAR(5)')

#Populate column using the stated conditions 
temp_conditions = '''
UPDATE CarSharing
SET Temp_Category = 
    CASE
        WHEN Temp_Feel <10 THEN 'Cold'
        WHEN Temp_Feel >= 10 AND Temp_Feel <= 25 THEN 'Mild'
        ELSE 'Hot'
    END
'''

cursor.execute(temp_conditions)
print("New Column 'Temp_Category' Successfully Created and Populated")

connection.close()