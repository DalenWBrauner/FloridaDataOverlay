"""
Update_Helper.py
This file is designed as a library for grabbing the appropriate
csv files in a given directory and returning them in a
format suitible for the database.

Written by Dalen W. Brauner
Last Maintained: 04/15/2014
"""
# Sources
FLORIDA_CHARTS = "http://www.floridacharts.com/"


## PUBLIC FUNC()S
def Prep_For_The_Database(how_so,csv):
    """
    Preps specific .csv files for entry into the database.
    """
    ERR = "Gimmie.py :: Prep_For_The_Database"
    ERR += " :: '"+how_so+"'\nERROR:\t"

    if   how_so == "Florida Charts_First Births.csv":
        print "FORMATTING '" + how_so + "'...",
        ERR += " :: 'Florida Charts_First Births.csv'\nERROR:\t"
        return _Format_FLCharts_Births(csv,ERR,0)

    elif how_so == "Florida Charts_Repeat Births.csv":
        print "FORMATTING '" + how_so + "'...",
        return _Format_FLCharts_Births(csv,ERR,1)
    
    elif how_so == "Florida Charts_AIDS Cases.csv":
        print "FORMATTING '" + how_so + "'...",
        return _Format_FLCharts_Diseases(csv,ERR,'AIDS Cases')

    elif how_so == "Florida Charts_HIV Cases.csv":
        print "FORMATTING '" + how_so + "'...",
        return _Format_FLCharts_Diseases(csv,ERR,'HIV Cases')

    elif how_so == "Florida Charts_HIVAIDS Crude.csv":
        print "FORMATTING '" + how_so + "'...",
        return _Format_FLCharts_Diseases(csv,ERR,'HIV+AIDS Deaths')

    elif how_so == "Florida Charts_HIVAIDS Age.csv":
        print "FORMATTING '" + how_so + "'...",
        return _Format_FLCharts_Diseases(csv,ERR,'HIV+AIDS Deaths Age-Adjusted')
        
##    elif how_so == "Florida Health_Births.csv":
##        print "FORMATTING '" + how_so + "' INCOMPLETE"
##        _debug_Print_The_Data(csv)
##        
##    elif how_so == "Florida Health_Diseases.csv":
##        print "FORMATTING '" + how_so + "' INCOMPLETE"
##        _debug_Print_The_Data(csv)
        
    else:
        ERR += "Hey, I'm not trained to format '"+how_so+"'!"
        raise Exception(ERR)


## PRIVATE FUNC()S
def _Format_FLCharts_Births(csv,ERR,repeat):
    
    # Cleans out " marks
    smudge = csv.find('"')
    while smudge != -1:
        csv = csv[:smudge] + csv[smudge+1:]
        smudge = csv.find('"')

    # Removes intentional commas
    comma = csv.find('grade,')
    while comma != -1:
        csv = csv[:comma+5] + csv[comma+6:]
        comma = csv.find('grade,')

    # Formats from String to Compound List
    csv = csv.split('\n')
    for d in xrange(len(csv)):
        csv[d] = csv[d].split(',')

    # Grab the year
    description = csv[1]
    for chunk in description:
        foundit = chunk.find("Year of Birth=")
        if foundit != -1:
            year = chunk[ foundit+14 : foundit+18 ]
            break
    if foundit == -1:
        ERR += "No year found!"
        raise Exception(ERR)

    # Remove useless rows
    useful = csv[3:-2]

    # Check all rows are the same length
    a = len(useful[0])
    for row in useful:
        b = len(row)
        if a != b:
            ERR += "Not all rows are the same length!"
            ERR += "\n\t(Are there too many commas in the csv?)"
            raise Exception(ERR)

    # Fill in age row
    suggestion = "COUNTIES"
    for idx in xrange(len(useful[0])):
        if  useful[0][idx] == '':
            useful[0][idx] = suggestion
        else:
            suggestion = useful[0][idx]

    # Convert to columns
    columns = []
    for age in xrange(len(useful[0])):
        a_column = []
        for row in useful:
            a_column.append(row[age])
        columns.append(a_column)

    # Remove 'Totals' columns
    colmod = 0
    for col in xrange(len(columns)):
        c = col - colmod
        if ('Total' in columns[c][0]) or 'Total' in columns[c][1]:
            columns.pop(c)
            colmod += 1

    # Convert to tuples in format:
    # (Year, County, Mother's Age, Mother's Education,
    # Source, Repeat, Births)
    final_tuples = []
    for COL in xrange(1,len(columns)-1):
        for ROW in xrange(2,len(columns[COL])):                
            tup = (year,                #Year
                   columns[0][ROW],     #County
                   columns[COL][0],     #Mother's Age
                   columns[COL][1],     #Mother's Education
                   FLORIDA_CHARTS,      #Source
                   repeat,              #Repeat
                   columns[COL][ROW])   #Births
            final_tuples.append(tup)

    print "COMPLETE!"
    return final_tuples


def _Format_FLCharts_Diseases(csv,ERR,topic):
    
    # Formats from String to Compound List
    csv = [item.split(",") for item in csv.split("\n")]
    
    # Grabs the list of years
    years = csv[1]
    for y in xrange(1,len(years)):
	if years[y] == '':
		years[y] = years[y-1]
    
    # Removes extraneous data
    rows = csv[3:-1]

    # The Unknown row does not have rates :(
    for r in xrange(2,len(rows[-1]),2):
        rows[-1][r] = '0'

    # Convert to tuples in format:
    # (Year, County, Topic, Source, Count, Rate)
    final_tuples = []
    for ROW in xrange(len(rows)):
        for COL in xrange(1,len(rows[0]),2):
            tup = (years[COL],          #Year
                   rows[ROW][0],        #County
                   topic,               #Topic
                   FLORIDA_CHARTS,      #Source
                   rows[ROW][COL],      #Count
                   rows[ROW][COL+1])    #Rate
            final_tuples.append(tup)

    print "COMPLETE!"
    return final_tuples

## DEBUG FUNC()S
def _debug_Print_The_Data(raw_csv):
    """It ain't pretty, but"""
    csv = [item.split(",") for item in raw_csv.split("\n")]
    for row in csv:
        output = '| '
        for cell in row:
            output += cell + '\t| '
        print output,'\n'
