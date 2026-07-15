# ----------------------------------------------
# -- Databases => SQlite => Update and Delete --
# ----------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

# Update Data
# cr.execute("UPDATE users SET name = 'Ali' WHERE user_id = 1")
# cr.execute("UPDATE users SET name = 'Mahmoud' WHERE user_id = 2")
# cr.execute("UPDATE users SET name = 'Sayed' WHERE user_id = 3")

# Delete Data
cr.execute("DELETE FROM users WHERE user_id = 4")

# Fetch Data
cr.execute("SELECT * FROM users")

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

# Save (commit) Changes
db.commit()

# Close Database Connection
db.close()

