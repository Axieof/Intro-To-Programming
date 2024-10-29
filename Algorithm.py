# Intro to computational thinking
# Assignment 1
# Team 3
# Tam, Nisha, Jerdel, Boris, Pritheev

# ========
# Imports
# ========
import csv
import tabulate

# ======================
# Variable Initialising
# ======================
Students = []
sortedStudents = []
pathToFile = '../records.csv'

# ======================
# Functions
# ======================

# printList - Prints lists in table form
def printList(dataset):
    if dataset:
        header = dataset[0].keys()
        rows = [x.values() for x in dataset]

        print(tabulate.tabulate(rows, header))
    else:
        print("Dataset is empty, cannot tabulate")

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

# getGroupSize
def getGroupSize():
    groupBool = True

    while groupBool:
        try:
            studentsPerGroup = input("Please enter the number of students per group (4-10)")
            
            studentsInt = int(studentsPerGroup)

            if 4<= studentsInt <= 10:
                groupBool = False
                return studentsInt
            else:
                print("Error: Group size must be between 4 and 10")

        except ValueError:
            print("Error: Please enter a number")
        except Exception as e:
            print(f"Error: Unexpected error - [{e}]")


# criteriaChecker
#def criteriaChecker():

# mainProcess
def mainProcess(pathToFile, studentsList, sortedStudentsList):

    # Step 1 - Load CSV File
    loadData(pathToFile, studentsList)

    # Step 2 - Sort based on Tutorial Group
    sortedStudents = sortStudents(sortedStudentsList, studentsList)

    # Step 3 - Get total number of tutorial groups
    totalGroups = getLastGroup(sortedStudents)

    # Step 4 - Ask for number of students per group (additional requirements)
    studentsNum = getGroupSize

    # Step 5 - Loop all tutorial groups
    for num in range(totalGroups):

        currentList = []
        count = 0

        for item in sortedStudents:
            if int(item['Tutorial Group'].split('-')[1]) == num+1 and num == 0:
                count += 1
                currentList.append(item)

        # Current List has 50 students from a tutorial group
        #printList(currentList)
            
        #male_list,female_list=genderSplit(currentList)
        
        # Step 6 - List with the school frequency in descending order
        newStudentList = schoolAffiliation(currentList)                 
        
        # Print in table format
        #printList(newStudentList)

        # Step 7 - Allocate into groups
        
        

        


    # Step 5 -


# Run Algorithm
mainProcess(pathToFile, Students, sortedStudents)
