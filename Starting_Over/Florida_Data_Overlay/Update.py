"""
Update.py
This file is designed to pull specified csv files in the given
directory and upload them as new entries to the database.

Written by Dalen W. Brauner
Last Maintained: 04/15/2014
"""


## IMPORTS
from Update_Helper import Prep_For_The_Database
from Overlay.models import Births


## STATIC VARS
from os import curdir as CURRENT_DIRECTORY
UPDATE_DIRECTORY = CURRENT_DIRECTORY + '\\Updates Go Here'
UPDATE_THESE = ["Florida Charts = First Births.csv",
                "Florida Charts = Repeat Births.csv",
                "Florida Charts = Diseases.csv",
                "Florida Health = Births.csv",
                "Florida Health = Diseases.csv"]
DATABASE_LOCATION = CURRENT_DIRECTORY + '\\SQLite3.db'


## FUNC()S
def Check_For_Updates(l1st):
    """
    Checks each filename in the given list for a csv file.
    Returns a Dictionary of each discovered csv as the Value
    and the filename as the Key.
    """
    DATA = {}
    for filename in l1st:
        result = Retrieve(UPDATE_DIRECTORY+"\\"+filename)
        if result:
            DATA[filename] = result
    
    return DATA

def Retrieve(filename):
    """
    Returns a List of the rows in the given csv.
    Returns None if the file does not exist.
    """
    try:
        with open(filename,"r") as f1le:
            raw_data = f1le.read()
    except IOError:
        return None
    return raw_data

def Upload(where_from,data):
    """
    Uploads data to the database; this is handled differently
    depending on which csv it came from.
    """
    if (where_from == UPDATE_THESE[0]) or (where_from == UPDATE_THESE[1]):
        for line in data:
            with Births(year=line[0],
                        county=line[1],
                        mothersAge=line[2],
                        mothersEdu=line[3],
                        source=line[4],
                        isRepeat=[5],
                        births=[6]) as New_Entry:
                New_Entry.save()
    else:
        ERR = "No upload procedure written for " + where_from
        raise TypeError(ERR)
        
def main():
    updates = Check_For_Updates(UPDATE_THESE)
        
    for key in updates:
        updates[key] = Prep_For_The_Database(key, updates[key])
        Upload(key, updates[key])

if __name__ == "__main__":main()
