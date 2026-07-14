# ------------------------------------------------------
# -- Databases => SQLite => Insert Data Into Database --
# ------------------------------------------------------
# - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# - commit => Save All Changes
# -------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

# Create The Tables And Fields
cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")

# Inserting Data
# cr.execute("INSERT INTO users(user_id, name) VALUES(1, 'Ahmed')")
# cr.execute("INSERT INTO users(user_id, name) VALUES(2, 'Ali')")
# cr.execute("INSERT INTO users(user_id, name) VALUES(3, 'Osama')")

my_list = ["Ahmed", "Sayed", "Mahmoud", "Ali", "Kamel", "Ali", "Ibrahim", "Sameh", "Enas"]

for i, user in enumerate(my_list):

    cr.execute(f"INSERT INTO users(user_id, name) VALUES({i + 1}, '{user}')")

# Save (commit) Changes
db.commit()

# Close Database 
db.close()