# TODO

'''
Expected Output:
---------------------------
Lavender Brown, born 1979
Colin Creevey, born 1981
Seamus Finnigan, born 1979
Hermione Jean Granger, born 1979
Neville Longbottom, born 1980
Parvati Patil, born 1979
Harry James Potter, born 1980
Dean Thomas, born 1980
Romilda Vane, born 1981
Ginevra Molly Weasley, born 1981
Ronald Bilius Weasley, born 1980
'''

from cs50 import SQL
from sys import argv
import os
import csv
import pandas as pd
from itertools import compress


# Validate command-line arguments.
if len(argv) != 2:
    print(f"Error there should be 2 argv, you have {argv}")
    exit(1)

# Gives access to this database
db = SQL("sqlite:///students.db")

house = argv[1]

rows = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first ", house)


for index, row in enumerate(rows):
    #   first, middle, last, birth = row["first"], row["middle"], row["last"], row["birth"]
    first, middle, last, _, birth = list(rows[:][index].values())[1:]
    print(f"{first} {middle + ' ' if middle else ''}{last}, born {birth}")


#DEBUGGERS

# Retrieve keys from list of dictionaries containing student info
# print(list(rows[:][8].keys())[1:])
# print(list(rows[:][8].values())[1:])

# print(rows)

# first, middle, last, _, birth = list(rows[:][0].values())[1:]
# print(f"\n{first}{middle if middle else ''} {last} was born in {birth}")