import gviz_api
import sqlite3

def get_me_a_DataTable(user_query, database_location):
    """Given a valid database query and the file location of the database,
    returns a Google DataTable object filled with database output."""

    # First, we establish a connection to the database.
    Connection = sqlite3.connect(database_location)
    SQL = Connection.cursor()

    # Second, we make the query.
    SQL.execute(user_query)
    database_output = SQL.fetchall()

    # Third, we establish what our columns are.
    query_cols = []
    for toople in SQL.description:
        query_cols.append(toople[0])

    # (We don't need this anymore.)
    Connection.close()

    # Fourth, we construct our schema:
    query_schema = {}
    for x in xrange(len(query_cols)):
        sql_type = type(database_output[0][x])
        if   sql_type == unicode:   datatable_type = "string"
        elif sql_type == float:     datatable_type = "float"    #"number"?
        elif sql_type == int:       datatable_type = "number"
        elif sql_type == long:      datatable_type = "number"
        elif sql_type == buffer:    datatable_type = "buffer"
        elif sql_type == None:      datatable_type = "string"
        else:                       datatable_type = "string"
        query_schema[query_cols[x]] = datatable_type

    # Fifth, we alter the format of the data to be google-charts friendly
    google_charts_input = []
    
    for entry in database_output:
        # For each entry, we need a dictionary, not a tuple.
        valid_entry = {}    
        # For each value in the entry, we need the column AND the value.
        for col in xrange(len(query_cols)):
            valid_entry[query_cols[col]] = entry[col]
        # Finally, we append the formatted data to our new list.
        google_charts_input.append(valid_entry)

    # Lastly, we convert our data to the chart, and return.
    query_datatable = gviz_api.DataTable(query_schema)
    query_datatable.LoadData(google_charts_input)

    return query_datatable
