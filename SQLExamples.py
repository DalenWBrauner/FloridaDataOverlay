def main_example():
    """This hopefully explains everything in
    http://docs.python.org/2/library/sqlite3.html
    but to those without a background in databases."""

    #
    ##
    ### Opens a connection to the database.
    import sqlite3
    Connection = sqlite3.connect('example.db')
    SQL = Connection.cursor()

    # Creates the 'roommates' table, where there's a
    # "name"   field, which is of type "text"
    # "gender" field, which is of type "text"
    # "age"   field, which is of type "int"
    SQL.execute('''CREATE TABLE roommates
                (name text, gender text, age int)''')


    # This is me creating data to be entered into the roommates table.
    # It matches the "name", "gender" and "age" format above.
    Dalen = ('Dalen', 'male', 19)

    # Alright, let's actually stick it into the database!
    # We can use ?s in place of the data we want and feed
    # it a tuple as an argument!
    SQL.execute('''INSERT INTO roommates
                VALUES (?, ?, ?)
                ''', Dalen)

    print "Let's see if that worked, shall we?"
    # This command selects everything in the roommates table
    SQL.execute('''
                SELECT *
                FROM roommates
                ''')
    output = SQL.fetchall()
    print type(output)
    print output
    print "There we have it!"
    print "Even though it's only one row, it's still a tuple inside a list.\n"


    # If I want to enter multiple rows into the database,
    # Each row is still a tuple and it's all inside a list!
    DalensRoomies = [('Michael Yoho', 'Male', 19),
                     ('Benjamin Gautier', 'Male', 21),
                     ('Andrew McGhee', 'Male', 19)]

    # This time we use SQL.executemany, but otherwise it's the same.
    SQL.executemany('''
                    INSERT INTO roommates
                    VALUES (?, ?, ?)
                    ''', DalensRoomies)

    print '''Let's see if that worked, but this time only
    check for my roommates who are 19.'''
    # This command selects everything in the roommates table
    # As long as their age field matches '19'
    SQL.execute('''
                SELECT *
                FROM roommates
                WHERE age=19
                ''')
    result = SQL.fetchall()
    for thing in result:
        print thing
    print "There you have it!"

    print "\nI have no idea what's up with these 'u's."
    # This deletes the table so the next time you run the code you don't get errors
    # for trying to create a table that already exists.
    SQL.execute('''DROP TABLE roommates''')

    #
    ##
    ### This tells the database to update with all of our changes.
    Connection.commit()

    #
    ##
    ### Close the connection.
    Connection.close()

main_example()
