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

# getLastGroup - Gets the tutorial group num of the last group
def getLastGroup(studentsList):
    return int(studentsList[-1]['Tutorial Group'].split('-')[1])

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

    # Step 3 - Get total number of tutorial groups
    totalGroups = getLastGroup(sortedStudents)

    # Step 4 - 
    for num in range(totalGroups):

        currentList = []

        for item in sortedStudents:
            if int(item['Tutorial Group'].split('-')[1]) == num+1:
                currentList.append(item)

        

        print(currentList)


    # Step 5 -


# Run Algorithm
mainProcess(pathToFile, Students, sortedStudents)
