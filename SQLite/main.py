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
# Insert values to table columms
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES (NULL, "Vitor Galves", 80)'
)
connection.commit()

# Finish SQL

cursor.close()                                  # Cursor and Connection need to be closed
connection.close()