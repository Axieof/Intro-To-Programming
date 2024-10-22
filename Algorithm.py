# Intro to computational thinking
# Assignment 1
# Team 3
# Tam, Nisha, Jerdel, Boris, Pritheev

# Imports
import csv
from collections import defaultdict

# Variable Initialising
Students = []
sortedStudents = []
pathToFile = '../records.csv'

# extractNum - Extracts numerical part from tutorial group
def extractNum(group):
    return int(group["Tutorial Group"].split('-')[1])

# Initialising defaultdict variable
tutorialGroup = defaultdict(list)

# loadData - Reading raw csv data
def loadData(filename, studentsList):
    with open(filename, mode='r') as recordsCSV:
        records = csv.DictReader(recordsCSV)
        
        for row in records:
            tempData = row['Tutorial Group']
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
loadData(pathToFile, Students)

sortedStudents = sortStudents(sortedStudents, Students)

for item in sortedStudents:
    print(item['Tutorial Group'])
