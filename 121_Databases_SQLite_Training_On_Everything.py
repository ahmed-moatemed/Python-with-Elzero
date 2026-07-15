# ---------------------------------------
# -- Databases => SQlite On Everything --
# ---------------------------------------

import sqlite3

def get_all_data():

    try:

        # Connect to Database
        db = sqlite3.connect("app.db")

        # Print Success Message
        print("Connected To Database Successfully")

        # Setting Up The Cursor
        cr = db.cursor()

        # Fetch Data From Database
        cr.execute("SELECT * FROM users")

        # Assign Data To Variable
        results = cr.fetchall()

        # Print Number Of Rows
        print(f"Database Has {len(results)} Rows.")

        # Printing Message
        print("Showing Data: ")

        # Loop On Results
        for element in results:

            print(f"UserID => {element[0]},", end=" ")

            print(f"Username => {element[1]}")

    except sqlite3.Error as er:

        print(f"Error Reading Data {er}")

    finally:

        if(db):

            # Close Database Connection
            db.close()

            print("Connection To Database Is Close")



get_all_data()