import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect('../db.sqlite3')
cursor = conn.cursor()

# SQL statement to insert a record
sql = "INSERT INTO dictionary_entry (word, definition, origin_language) VALUES (?, ?, ?)"
record = ('naija', 'Slang for Nigeria', 'Pigeon')  # Replace 'value1' and 'value2' with your actual data

# Execute the SQL statement
cursor.execute(sql, record)

# Commit the changes and close the connection
conn.commit()
conn.close()
