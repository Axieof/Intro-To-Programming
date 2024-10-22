# Intro to computational thinking
# Assignment 1
# Team 3
# Tam, Nisha, Jerdel, Boris, Pritheev

# ========
# Imports
# ========
import csv

# ======================
# Variable Initialising
# ======================
Students = []
sortedStudents = []
pathToFile = '../records.csv'

# ======================
# Functions
# ======================

# extractNum - Extracts numerical part from tutorial group
def extractNum(group):
    return int(group["Tutorial Group"].split('-')[1])

# loadData - Reading raw csv data
def loadData(filename, studentsList):
    with open(filename, mode='r') as recordsCSV:
        records = csv.DictReader(recordsCSV)
        
        for row in records:
            studentsList.append(row)

# sortStudents - 
def sortStudents(sortList, studentsList):
    sortList = sorted(studentsList, key=extractNum)
    return sortList

# genderSplit

# schoolAffiliation

# currentCGPA

# exportData

# mainProcess
def mainProcess(pathToFile, studentsList, sortedStudentsList):

    # Step 1 - Load CSV File
    loadData(pathToFile, studentsList)

    # Step 2 - Sort based on Tutorial Group
    sortedStudents = sortStudents(sortedStudentsList, studentsList)

    # Step 3 - 

    # Step 4 - 

    # Step 5 -


# Run Algorithm
mainProcess(pathToFile, Students, sortedStudents)
