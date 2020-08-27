# TODO
# course: CS50
# problem set: 7
# date: 08/07/2020
# username: Empathineer
# name: Carissa Chan
# description: write a program that imports data from a CSV spreadsheet and produce class rosters


from cs50 import SQL
from sys import argv
import os
import csv
import pandas as pd

"""
This program should accomplish the following:
1) If the incorrect number of command-line arguments.
2) Read in csv file
3) Parse name for each row.
3) Insert each student into the students table of the students.db to
produce a class roster from the dataset
4) Print the class roster per format below.

CSV format head
                      name       house  birth
0          Adelaide Murton   Slytherin   1982
1             Adrian Pucey   Slytherin   1977
2        Anthony Goldstein   Ravenclaw   1980
3            Blaise Zabini   Slytherin   1979
4           Cedric Diggory  Hufflepuff   1977

"""


# Validate command-line arguments.
if len(argv) != 2:
    print(f"Error there should be 2 argv, you have {argv}")
    exit(1)

path = argv[1]

# Gives access to this database
db = SQL("sqlite:///students.db")

def split_name(student):
    names = student.split()
    return names if len(names) >= 3 else [names[0], None, names[1]]

def add_entry(row):
    student = row['name'].split()
    first, *others = student[0], student[1:]
    middle = student[1] if (len(student) > 2) else None
    last = student[-1]

    db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
            first, middle, last, row['house'], row['birth']
    )


# __location__ = os.path.realpath(
#     os.path.join(os.getcwd(), os.path.dirname('characters.csv')))

# with open(os.path.join(__location__, 'characters.csv')) as f:
# with open(path) as in_file:
with open(argv[1], "r") as in_file:
    characters = pd.read_csv(in_file)
    # reader = csv.DictReader(in_file)
    # print(characters)

    for index, row in characters.iterrows():
        add_entry(row)
        # names = split_name(row['name'])
        # student = characters.iloc[row][0]
        # student.append()
        # db.execute("INSERT INTO students VALUES(?, ?, ?, ?, ?)",
        #     names[0], names[1], names[2], row["house"], row["birth"]
        # )
        # print("Student Number {}: {}".format(index, row['name']))

  # for row in reader:
    #     names = split_name(row['name'])
    #     db.execute("INSERT INTO students VALUES(?, ?, ?, ?, ?)",
    #         names[0], names[1], names[2], row["house"], row["birth"]
    #     )


    # # DEBUG TESTER
    # tester = student[8]
    # print(tester)
    # print(student[8])



    # print(characters.iloc[8][0])

    # print("Characters type: ", type(characters))

    # student = []

    # func_dict = {
    #     'cond_mid' : handle_middle,
    #     'cond_none' : handle_no_middle,
    # }

    # print(type(characters.iloc[0]))

