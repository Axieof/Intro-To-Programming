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
pathToOutput = './FCEC_3_Pritheev.csv'

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

def schoolAffiliation(male_list, female_list):
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

# schoolAffiliation
def oldSchoolAffiliation(studentList):
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

# calculateOptimalDistribution
def calculateOptimalDistribution(male_list, female_list, studentsNum):
    numStudents = 50  # Assuming each tutorial group has 50 students
    numTeams = numStudents // studentsNum
    remainder = numStudents % studentsNum

    if remainder > 0:
        normalTeams = numTeams - remainder
        remainingTeams = remainder
        print(f"Creating {normalTeams} teams of {studentsNum} and {remainingTeams} teams of {studentsNum + 1}")
    else:
        normalTeams = numTeams
        remainingTeams = 0
        print(f"Creating {normalTeams} teams of {studentsNum}")

    totalMales = len(male_list)
    totalFemales = len(female_list)

    team_gender_template = []
    for i in range(normalTeams):
        male_count = min(totalMales // normalTeams, studentsNum // 2 + (studentsNum % 2))
        female_count = studentsNum - male_count
        team_gender_template.append((male_count, female_count))

    for i in range(remainingTeams):
        male_count = min(totalMales // remainingTeams, (studentsNum + 1) // 2 + ((studentsNum + 1) % 2))
        female_count = (studentsNum + 1) - male_count
        team_gender_template.append((male_count, female_count))

    print("Optimal gender distribution per team (M,F):", team_gender_template)
    return team_gender_template
  
def verifyAndAdjustTeams(teams):
    for team in teams:
        male_count = sum(1 for student in team if student['Gender'] == 'Male')
        female_count = len(team) - male_count
        
        # Verify gender balance
        if abs(male_count - female_count) > 1:
            print(f"Adjusting gender balance in team: {team}")
            # Implement logic to swap students with other teams if possible

        # Verify school diversity
        school_counts = {}
        for student in team:
            school = student['School']
            school_counts[school] = school_counts.get(school, 0) + 1
        max_school_count = max(school_counts.values())
        
        if max_school_count > len(team) // 2:
            print(f"Adjusting school diversity in team: {team}")
            # Implement logic to swap students from the dominant school with other teams

    print("Teams adjusted to meet criteria.")
    return teams

# createGroups - Assign groupings, going back and forth between male and females, while ensuring school diversity
def createGroups(male_schools, female_schools, group_size):
    groups = [] # final groupings
        
    # Determine the number of males and females to add based on their availability and group size
    total_males = sum(len(students) for students in male_schools.values())
    total_females = sum(len(students) for students in female_schools.values())

    print(f"Tutorial Group Gender Distribution is M:{total_males}, F:{total_females}")

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

    #groups = criteriaChecker(groups, max_females, max_males)
    
    return groups

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

# exportCSV
def exportCSV(groups):
    with open(pathToOutput, mode='a', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["Tutorial Group","Student ID", "School", "Name", "Gender", "CGPA", "Assigned Team"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        csv_file.seek(0, 2)
        if csv_file.tell() == 0:
            writer.writeheader()

        for i, group in enumerate(groups, start=1):
                # print(f"Group {i}:")
                for student in group:
                    # print(f"{student['Name']} from {student['School']} ({student['Gender']})")
                    student['Assigned Team'] = i
                    writer.writerow(student)

# mainProcess
def mainProcess(pathToFile, studentsList, sortedStudentsList):

    # Step 1 - Load CSV File
    loadData(pathToFile, studentsList)

    # Step 2 - Sort based on Tutorial Group
    sortedStudents = sortStudents(sortedStudentsList, studentsList)

    # Step 3 - Get total number of tutorial groups
    totalGroups = getLastGroup(sortedStudents)

    # Step 4 - Ask for number of students per group (additional requirements)
    studentsNum = getGroupSize()

    # Step 5 - Loop all tutorial groups
    for num in range(totalGroups):

        currentList = []
        count = 0

        for item in sortedStudents:
            if int(item['Tutorial Group'].split('-')[1]) == num+1:
                count += 1
                currentList.append(item)

        # Current List has 50 students from a tutorial group
        printList(currentList)
            
        # Step 6 - Split by gender
        male_list,female_list = genderSplit(currentList)

        # Step 7 - Sort the genders by their schools
        male_schools, female_schools = schoolAffiliation(male_list,female_list)

        # Step 8 - Assign to teams
        groups = createGroups(male_schools, female_schools, studentsNum)

        # Step 9 - Check that teams meet criteria

        # Step 10 - Export to CSV
        exportCSV(groups)

        break

# Run Algorithm
mainProcess(pathToFile, Students, sortedStudents)
