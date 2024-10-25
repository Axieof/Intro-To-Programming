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
pathToFile = 'records.csv'

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
def genderSplit(studentlist):
    male_list = []
    female_list = []
    for student in studentlist:
        if student["Gender"]== "Male":
            male_list.append(student)
        else:
            female_list.append(student)
    return male_list, female_list

# schoolAffiliation
def schoolAffiliation(studentList):
    schoolCount = {}
    for student in studentList:
        school = student['School']
        if school in schoolCount:                       # counting the recurrence of different schools
            schoolCount[school] += 1
        else:
            schoolCount[school] = 1
                  
    schoolCountList = list(schoolCount.items())
    for i in range(len(schoolCountList)):
        for j in range(i + 1, len(schoolCountList)):
            if schoolCountList[i][1] < schoolCountList[j][1]:
                schoolCountList[i], schoolCountList[j] = schoolCountList[j], schoolCountList[i]     # sorting by school with the highest frequency
                
    newStudentList = []
    for tuples in schoolCountList:
        school = tuples[0]
        for student in studentList:
            if student['School'] == school:
                newStudentList.append(student)
                
    return newStudentList
    
                        
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
            
        male_list,female_list=genderSplit(currentList)
        
        newStudentList = schoolAffiliation(currentList)                 # List with the school frequency in descending order
        # Current List has 50 students from a tutorial group
        #print(currentList)
        
        # Step 5 - Split by gender
        

        


    # Step 5 -


# Run Algorithm
mainProcess(pathToFile, Students, sortedStudents)
