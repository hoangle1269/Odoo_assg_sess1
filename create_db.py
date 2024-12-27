import sqlite3

# Step 1: Connect to SQLite (or create the database file if it doesn't exist)
conn = sqlite3.connect('example.db')  # This creates a file named 'example.db'

# Step 2: Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Step 3: Create a table (if it doesn't already exist)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        age INTEGER
    )
''')

# Step 4: Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")
