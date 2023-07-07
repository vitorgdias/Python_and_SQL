import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'DELETE FROM {TABLE_NAME} '            # Delete from table the row that the id number correspond to 4
    'WHERE id = "4"'                        # The INTERGER don't need to be under "", just strings need.
)
connection.commit()

cursor.execute(
    f'UPDATE {TABLE_NAME} '            # Delete from table the row that the id number correspond to 4
    'SET name="OTHER" '                      # Update the column name where id = 11 to "OTHER"
    'WHERE id = "11"'                       # The INTERGER don't need to be under "", just strings need.
)
connection.commit()

cursor.execute(
    f'UPDATE {TABLE_NAME} '            # Delete from table the row that the id number correspond to 4
    'SET name="ANOTHER", weight=15.47 '      # Update the column name and weight where id = 10
    'WHERE id = "10"'                       # The INTERGER don't need to be under "", just strings need.
)
connection.commit()

cursor.close()
connection.close()