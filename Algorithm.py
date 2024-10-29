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
    
# createGroups - Assign groupings, going back and forth between male and females, while ensuring school diversity
def createGroups(male_schools, female_schools, group_size=5):
    groups = [] # final groupings
        
    # Determine the number of males and females to add based on their availability and group size
    total_males = sum(len(students) for students in male_schools.values())
    total_females = sum(len(students) for students in female_schools.values())

    if total_females > total_males:
        max_females = (group_size + 1) // 2 
        max_males = group_size - max_females
    else:
        max_males = (group_size + 1) // 2 
        max_females = group_size - max_males
    
    # While there are students left in bucket
    while any(male_schools.values()) or any(female_schools.values()):
        # Reset create_group and count for next iteration
        create_group = [] # temp group
        male_count, female_count = 0, 0
        temp_males, temp_females = [], []  # Track students to remove on success
        
        while len(create_group) < group_size:
            added = False

            if male_count < max_males:
                # For male
                # Check before assigning group: 1. number of males in group matches calculated availability, 2. ensures no more than 1 from same school
                for school, male in male_schools.items():
                    if male and not any(s['School'] == school for s in create_group):
                        # Removes the student being added to group from the bucket of students
                        male_to_add = male[0]
                        create_group.append(male_to_add)
                        temp_males.append((school,male_to_add))  # Mark for removal on success
                        male_count += 1
                        added = True
                        break

            elif female_count < max_females:
                # Repeat for female
                for school, female in female_schools.items():
                    if female and not any(s['School'] == school for s in create_group):
                        female_to_add = female[0]
                        create_group.append(female_to_add)
                        temp_females.append((school,female_to_add)) 
                        female_count += 1
                        added = True
                        break

            # If neither a male nor female could be added, switch turns and try again
            if not added:
                break
        
        # Only remove students if the group is fully formed, else exit if can't fill a complete group
        if len(create_group) == group_size:
            for school, male in temp_males:
                male_schools[school].pop(0)
            for school, female in temp_females:
                female_schools[school].pop(0)
            groups.append(create_group)
        else:
            break

    # Add leftover students in groups if (50 % group_size != 0)
    leftovers = []
    for school, male_list in male_schools.items():
        leftovers.extend(male_list)
    for school, female_list in female_schools.items():
        leftovers.extend(female_list)

    while leftovers:
        groups.append(leftovers[:group_size])
        leftovers = leftovers[group_size:]

    
    return groups
                        
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

def nishaschoolAffiliation(male_list, female_list):
    # dictionary lists
    # Example:
    #     male_schools = males:  {
    #       'CCDS': [{'Tutorial Group': 'G-1', 'Student ID': '5002', 'School': 'CCDS', 'Name': 'Aarav Singh', 'Gender': 'Male', 'CGPA': '4.02'}, {'Tutorial Group': 'G-1', 'Student ID': '235', 'School': 'CCDS', 'Name': 'Ming Zhang', 'Gender': 'Male', 'CGPA': '4.06'}], 
    #       'EEE': [{'Tutorial Group': 'G-1', 'Student ID': '3628', 'School': 'EEE', 'Name': 'Omer Ahmed', 'Gender': 'Male', 'CGPA': '4.06'}] 
    #       }
    male_schools = {}
    female_schools = {}

    # Adds the list of male/female student into dictionary based on their school
    for male in male_list:
        school = male["School"]
        if school not in male_schools:
            male_schools[school] = []
        male_schools[school].append(male)
    for female in female_list:
        school = female["School"]
        if school not in female_schools:
            female_schools[school] = []
        female_schools[school].append(female)

    return male_schools, female_schools

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
            
        # Step 6 - Split by gender
        male_list,female_list=genderSplit(currentList)
        
        # Step 7 - List with the school frequency in descending order
        malesStudentList = schoolAffiliation(male_list)
        femalesStudentList = schoolAffiliation(female_list)   

        #male_schools, female_schools = nishaschoolAffiliation(male_list,female_list)
        #printList(male_schools)
        #printList(female_schools)  

        printList(malesStudentList)
        printList(femalesStudentList)    
        break          
        
        # Print in table format
        #printList(newStudentList)

        # Step 7 - Allocate into groups
        
        

        


    # Step 5 -


# Run Algorithm
mainProcess(pathToFile, Students, sortedStudents)
