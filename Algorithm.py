# Intro to computational thinking
# Assignment 1
# Team 3
# Tham, Nisha, Jerdel, Boris, Pritheev

# Imports
import csv
from collections import defaultdict

# Variable Initialising
tutorialList = []
indexList = []
schoolList = []
nameList = []
genderList = []
gpaList = []
Students = []
pathToFile = '../records.csv'

# extractNum - Extracts numerical part from tutorial group
def extractNum(group):
    return int(group.split('-')[1])

# Initialising defaultdict variable
tutorialGroup = defaultdict(list)

# loadData - Reading raw csv data
def loadData(filename):
    with open(filename, mode='r') as recordsCSV:
        records = csv.DictReader(recordsCSV)
        
        for row in records:
            tempData = row['Tutorial Group']
            tutorialGroup[tempData].append(row)



# sortStudents - 

# genderSplit

# schoolAffiliation

# currentCGPA

# exportData

# mainProcess
loadData(pathToFile)

print(tutorialGroup)
