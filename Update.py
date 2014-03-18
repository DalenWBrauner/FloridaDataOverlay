"""
Update.py
This file is designed to pull certain csv files in the given
directory and upload them as new entries to the database.

Written by Dalen W. Brauner
Last Maintained: 03/17/2014
"""
from Gimmie import Check_For_Updates, Prep_For_The_Database
import sqlite3
CONNECTION = sqlite3.connect('SQLite.db')
SQL = CONNECTION.cursor()

#
##
### Data Upload Functions
def Upload(where_to,data):
    if   where_to == "Florida Charts_First Births.csv" \
       or where_to == "Florida Charts_Repeat Births.csv":
        SQL.execute("BEGIN;")
        SQL.executemany("""INSERT INTO births VALUES (?,?,?,?,?,?,?);""", data)
##        SQL.executemany("""
##                        BEGIN;
##                        INSERT INTO births VALUES (?,?,?,?,?,?,?);
##                        COMMIT;""", data)
##        SQL.execute("COMMIT;")
        CONNECTION.commit()
        print "SUCCESS QUESTION MARK?"
        SQL.execute("""SELECT * FROM births WHERE county='Washington' AND Mothers_Age=42""")
        print SQL.fetchall()

    else:
        print "No good."
        

#
##
### Main Function

def main():
    UPDATE_THESE = ["Florida Charts_First Births.csv",
                    "Florida Charts_Repeat Births.csv",
                    "Florida Charts_Diseases.csv",
                    "Florida Health_Births.csv",
                    "Florida Health_Diseases.csv"]
    updates = Check_For_Updates(UPDATE_THESE)
    if len(updates) == 0:
        print "No updates!"
        quit()  # If there aren't any updates, don't waste your time!
    for key in updates:
        updates[key] = Prep_For_The_Database(key,updates[key])
        Upload(key,updates[key])

    CONNECTION.close()


if __name__ == "__main__":main()
