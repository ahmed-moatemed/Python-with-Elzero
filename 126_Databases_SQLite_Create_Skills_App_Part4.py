# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 3 --
# -----------------------------------------------------

# import SQLite and Connection and Setting up cursor
import sqlite3

db = sqlite3.connect("app.db")

cr = db.cursor()

# Commit and Close Method
def commit_and_close():
    """Commit Changes And Close Connection To Database"""
    db.commit()
    db.close()
    print("Connection To Database Is Close")

# My User id 
uid = 1

# Input Big Message
input_message = """
What do you want to do?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option: 
"""

# Input Option Choose
user_input = input(input_message).strip().lower()

# Command List 
commands_list = ["s", "a", "d", "u", "q"]

# Defind The Methods
def show_skills():

    cr.execute(f"select * from skills where user_id = {uid}")

    result = cr.fetchall()

    print(f"You Have {len(result)} Skills.")

    if len(result) > 0:

        print("Showing Skills With Progress: ")

    for row in result:

        print(f"Skill => {row[0]}", end=" ")
        print(f"Progress => {row[1]}%")
    
    commit_and_close()

def add_skill():

    sk = input("Write Skill Name: ").strip().capitalize()

    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}'")

    result = cr.fetchone()

    if result == None:

        print("Skill Is Not Exists in DB, and You Can Add It :).")

        prog = input("Write Skill Progress: ").strip()

        cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")

    else:

        print("Skill Is Exists, You Can't Add It.")

        ans = input("Do You Want Update This Progress? y/n ").strip().lower()

        if ans == 'y' or ans == 'yes':

            prog = input("Write The New Skill Progress: ").strip()

            cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")
        

    commit_and_close()

def delete_skill():

    sk = input("Write Skill Name: ").strip().capitalize()

    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")

    commit_and_close()

def update_skill():

    sk = input("Write Skill Name: ").strip().capitalize()

    prog = input("Write The New Skill Progress: ").strip()

    cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")

    commit_and_close()


# Check If Command Is Exists
if user_input in commands_list:

    if user_input == "s":

        show_skills()
    
    elif user_input == "a":

        add_skill()

    elif user_input == "d":

        delete_skill()

    elif user_input == "u":

        update_skill()
    
    else:

        print("App Is Closed.")
        commit_and_close()

else:

    print(f"Sorry This Command \"{user_input}\" Is Not Found")

