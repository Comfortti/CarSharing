#Importing sqlite3 and connecting to the database
import sqlite3

connection = sqlite3.connect('CarSharing.db', isolation_level=None)
cursor = connection.cursor()

#Create a table called 'Time'
time = '''
CREATE TABLE IF NOT EXISTS Time ( 
Timestamp TEXT, 
Hour INTEGER, 
Weekday INTEGER, 
Month INTEGER
)'''

cursor.execute(time)
print('Time table successfully created')

#sqlite3 has a limited set of directives, therefore we need to use the numerica output
#and then assign those outputs to their respective week and month names 
#first we populate the columns making sure to convert from a string to an integer 
timestamp = '''
INSERT INTO Time (Timestamp, Hour, Weekday, Month)
SELECT Timestamp, 
    CAST(strftime('%H', Timestamp) AS INTEGER) AS Hour, 
    CAST(strftime('%w', Timestamp) AS INTEGER) AS Weekday, 
    CAST(strftime('%m', Timestamp) AS INTEGER) AS Month
FROM CarSharing
'''
cursor.execute(timestamp)
print('Timestamp records successfully inserted into Time table')

# Now to convert the numeric output to their respective week or month names 
cursor.execute('SELECT * FROM Time')
rows = cursor.fetchall()

# Map weekday numbers and month numbers to names
weekday_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
month_names = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Update the Weekday and Month columns with their respective names that were mapped
for row in rows:
    timestamp = row[0]
    weekday_number = row[2]
    month_number = row[3]
    
    weekday_name = weekday_names[int(weekday_number)] 
    month_name = month_names[int(month_number)] 
    
    cursor.execute('''
        UPDATE Time
        SET Weekday = ?,
            Month = ?
        WHERE Timestamp = ?
    ''', (weekday_name, month_name, timestamp))

#check that everything was successfully mapped 
cursor.execute('SELECT * FROM Time')
TimeTable = cursor.fetchmany(size=5) 
print(TimeTable)

connection.close()