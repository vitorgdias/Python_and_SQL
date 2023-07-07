import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent                # Import the path to root directory
DB_NAME = 'db.sqlite3'                          # Database name
DB_FILE = ROOT_DIR / DB_NAME                    # Path to DB_NAME
TABLE_NAME = 'customers'                        # Define the table name

connection = sqlite3.connect(DB_FILE)           # Can be named as con, receive the full path of the file
cursor = connection.cursor()                    # Execute queries
# Create the table
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'  
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'     # Set one key for each data automatically (it's not a sequence)
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()
# This command bellow delete the IDs and restart the sequence in DB
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()
# Insert values to table columns
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES (NULL, "Vitor Galves", 80)'
)
connection.commit()

'''
# CAUTION: In SQLite, if use DELETE without WHERE all values will be deleted. To delete one row is needed to add the column ID.
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()

# After use DELETE in this DB, the ID will continue increasing the values beacause of the AUTOINCREMENT

# This command bellow delete the IDs and restart the sequence in DB
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()
'''

# Insert many values to table columns
# CAUTION: This kind of values inserted is just if you insert values in the code, if you receive values from another user, be carefull of sql injections
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES (NULL, "João", 100), (NULL, "Guilherme", 70.5)'  # Is possible to add more than one data to the DB
)
connection.commit()

# Using placeholder in SQL insert, to avoid SQL injection
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '               # Id insert is not necessary
    'VALUES '
    '(?, ?)'                        # ? is used as a placeholder, to avoid SQL Injection
)
cursor.execute(sql, ['João', 100])
cursor.executemany(sql, (('João', 100), ('Guilherme', 70)))     # Is preferred to have tuple of tuple, but you can use lists fo lists too [[X,Y],[A,B]] to executemany
connection.commit()
print(sql)

# Dictionaries can be used to execute queries, in some cases will be more interesting
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '               
    'VALUES '
    '(:name, :weight)'          # Is not common, but you can use different labels to define the dictionary '(:other, :another)'
)
cursor.execute(sql, {'name':'José', 'weight': 100})
# Adding a Tupple of dictionaries
cursor.executemany(sql, (               
    {'name':'Jeronimo', 'weight': 80},
    {'name':'Jorge', 'weight': 50},
    {'name':'Jeca', 'weight': 70},
    {'name':'Mario', 'weight': 68.5}
    )
)
connection.commit()
if __name__ == '__main__':
    print(sql)
# Finish SQL
# Cursor and Connection need to be closed
cursor.close()                                  
connection.close()
