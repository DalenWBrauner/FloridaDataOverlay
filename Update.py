"""
Update.py
This file is designed to retrieve any and all csv files in
the given directory and read them as new entries to the database.

Written by Dalen W. Brauner
Last Maintained: 03/17/2014
"""

#
##
### Assist Functions

def Check_For_Updates(l1st):
    """
    Checks each filename in the given list for a csv file.
    Returns a Dictionary of each discovered csv as the Value
    and the filename as the Key.
    """
    
    DATA = {}
    for filename in l1st:
        result = Retrieve(filename)
        if result:
            DATA[filename] = result
    
    return DATA

def Retrieve(filename):
    """
    Returns a List of the rows in the given csv.
    Returns None if the file does not exist.
    """

    # Makes the attempt
    try:
        # Retrieves file
        f1le = open(filename,"r")
        raw_data = f1le.read().split('\n')
        f1le.close()

    # Returns None if the file DNE
    except IOError:
        return None

    # Formats from string to compound list
    fixed_data = raw_data[:]
    for d in xrange(len(raw_data)):
        fixed_data[d] = raw_data[d].split(',')
    
    return fixed_data

def Prep_For_The_Database(how_so,csv):
    if   how_so == "Florida Charts_First Births.csv":
        print "FORMATTING '" + how_so + "' INCOMPLETE"
        
    elif how_so == "Florida Charts_Repeat Births.csv":
        print "FORMATTING '" + how_so + "' INCOMPLETE"
        
    elif how_so == "Florida Charts_Diseases.csv":
        print "FORMATTING '" + how_so + "' INCOMPLETE"
        
    elif how_so == "Florida Health_Births.csv":
        print "FORMATTING '" + how_so + "' INCOMPLETE"
        
    elif how_so == "Florida Health_Diseases.csv":
        print "FORMATTING '" + how_so + "' INCOMPLETE"
        
    else:
        ERR = "Hey, I'm not trained to format '"+how_so+"'!"
        raise Exception(ERR)

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
    for key in updates:
        updates[key] = Prep_For_The_Database(key,updates[key])

#
##
### Debug Functions

def _debug_Print_The_Data(csv):
    """It ain't pretty, but"""
    for row in fixed_data:
        output = '| '
        for cell in row:
            output += cell + '\t| '
        print output,'\n'

if __name__ == "__main__":  main()
