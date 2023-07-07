import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')        # Some queries is more easy to do in SQL language, but is possible to do in Python

for row in cursor.fetchall():                        # Return all rows in the DB with columns id, name and weight
    _id, name, weight = row
    print(_id, name, weight)

cursor.execute(f'SELECT * FROM {TABLE_NAME} '        # This queries only select the row where the id is 3
    'WHERE id = "3"'                   
)        
row = cursor.fetchone()                              # Return the first value in the DB (or select with where)
print(row)

row = cursor.fetchone()                              # Is possible to return like this way too
_id, name, weight = row
print(_id, name, weight)

cursor.close()
connection.close()