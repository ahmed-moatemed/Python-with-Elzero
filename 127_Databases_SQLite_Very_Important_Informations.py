# -------------------------------------------------------
# -- Databases => SQLite => Very Important Information --
# -------------------------------------------------------

# Import SQLite
import sqlite3

# Connection To Database
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

my_tuple = ('Pascal', '70', '4')

# Insert Data
# cr.execute("insert into skills values(?, ?, ?)", my_tuple)

# Fetch Data 
# cr.execute("select * from skills order by name limit 4 offset 2") # read from row 3 تجاهل اول 2 صف

# cr.execute("select * from skills where user_id > 1")

# cr.execute("select * from skills where user_id in(1, 3)")

cr.execute("select * from skills where user_id not in(1, 3)")


# Assign Data
results = cr.fetchall()

# Loop in Data and Show
for row in results:

    print(f"Skill Name => {row[0]},", end=" ")
    print(f"Skill Progress => {row[1]},", end=" ")
    print(f"User Id => {row[2]}")


# Save Data
db.commit()

# Close Database
db.close()