# ------------------------------------------------------
# -- Databases => SQLite => Retrieve Data From Database --
# ------------------------------------------------------
# - fetchone => Returns a Single Record or None If no More rows are Available
# - fetchall => fetches All the rows os query results. It returns all the rows
#             as a list of tuples. an empty list is returned if there is no record to fetch.
# - fetchmany(size) =>
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

# Fetch Data
cr.execute("SELECT * FROM users")

# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())

# print(cr.fetchall())

print(cr.fetchmany(3))


# Save (commit) Changes
db.commit()

# Close Database 
db.close()