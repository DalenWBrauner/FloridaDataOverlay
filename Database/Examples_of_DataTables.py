import gviz_api

example_schema = {
    "name": ("string", "Full Name"),
    "gender": ("string", "Gender"),
    "age":("number", "Age")
    }
example_data = [
    {"name": 'Dalen Brauner', "gender": 'Male', "age": 19},
    {"name": 'Michael Yoho', "gender": 'Male', "age": 19},
    {"name": 'Benjamin Gautier', "gender": 'Male', "age": 21},
    {"name": 'Andrew McGhee', "gender": 'Male', "age": 19},
    {"name": 'Ethan Block', "gender": 'Male', "age": 20}
    ]

example_datatable = gviz_api.DataTable(example_schema)
example_datatable.LoadData(example_data)


# If the above code runs, great. That means it's time to get started.
# If the below code runs, shiit; we're in BUSINESS!
import sqlite3
Connection = sqlite3.connect('SQLite.db')
SQL = Connection.cursor()

# Let's pretend this string came from the user
user_query = '''
            SELECT *
            FROM births
            WHERE County='Unknown'
            '''

# Everything from here down should work FOR ALL queries.
SQL.execute(user_query)
database_output = SQL.fetchall()


# Before anything else, we need to know our columns.
query_cols = []
for toople in SQL.description:
    query_cols.append(toople[0])


###
print query_cols
### Which should come out to ["year","county","age","edu","source","repeat","births"]

# Next, we construct our schema:
query_schema = {}
for x in xrange(len(query_cols)):
    sql_type = type(database_output[0][x])
    if   sql_type == unicode:   datatable_type = "string"
    elif sql_type == float:     datatable_type = "float"    #"number"?
    elif sql_type == int:       datatable_type = "number"
    elif sql_type == long:      datatable_type = "number"
    elif sql_type == None:      raise TypeError("TELL THE DEVELOPER TO IMPLEMENT 'NULL COMPATIBILITY'.")
    elif sql_type == buffer:    datatable_type = "buffer"
    else:
        ERR = "Apparently my code doesn't like",str(sql_type),"very much."
        raise TypeError(ERR)
    query_schema[query_cols[x]] = datatable_type

# BAM! WE'RE DONE WITH THE SCHEMA!

###
print query_schema
### Which should come out to:
### query_schema = {
###     "year": ("number", "Year of Birth"),
###     "county": ("string", "Mother's Home County"),
###     "age": ("number", "Mother's Age"),
###     "edu": ("text", "Mother's Education Level"),
###     "source": ("text", "Source"),
###     "repeat": ("boolean", "Repeat Pregnancy"),
###     "births": ("number", "Number of Births")
###     }



## Quick Recap:
## The database spits out a list; this is the 'cropped' table.
## Each item in that list is a tuple; this is a 'row', or 'entry' in the table.
## Each item in that tuple is a value; whether it be that entry's name or age.
##
## Is that what we need?
## We need to provide a list; this is the 'cropped' table.
## Each item in that list is a dictionary; this is a 'row' or 'entry' in the table.
## Each key in that dictionary is a column name; each value is that corresponding value.
##
## This might not be hard at all, but the computer won't like it. (One loop per datapoint.)
## So here's how we fix our data:
google_charts_input = []

# For each entry, we need a dictionary, not a tuple.
for entry in database_output:        
    valid_entry = {}
    
    # For each value in the entry, we need the column AND the value.
    for col in xrange(len(query_cols)):
        valid_entry[query_cols[col]] = entry[col]

    # Now that that's done, stick the entry in our list...
    google_charts_input.append(valid_entry)

# BAM! WE'RE DONE WITH THE DATA!

query_datatable = gviz_api.DataTable(query_schema)
query_datatable.LoadData(google_charts_input)

Connection.close()
print 'ALL DONE!'
