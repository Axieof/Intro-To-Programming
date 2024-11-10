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

def schoolChecker(male_schools, female_schools, group_size, total_students=50):
    """
    Determines the maximum number of students from each school that can be placed in each team.
    Prints the total count per school and the calculated distribution.
    """
    school_distribution = {}

    # Combine male and female students by school
    for school, students in male_schools.items():
        school_distribution[school] = school_distribution.get(school, 0) + len(students)
    for school, students in female_schools.items():
        school_distribution[school] = school_distribution.get(school, 0) + len(students)

    # Calculate maximum allowed students per school in each team
    max_students_per_school = {}
    num_teams = total_students // group_size

    print("Total students per school:")
    for school, count in school_distribution.items():
        print(f" - {school}: {count} students")
        
        # Calculate base allocation per team and distribute any remainder
        if count <= num_teams:
            # If fewer students than teams, assign 1 per team
            max_students_per_school[school] = (1, 0)
        else:
            max_per_team = count // num_teams
            leftover = count % num_teams  # Leftover students to be distributed
            max_students_per_school[school] = (max_per_team, leftover)

    print("\nMax students per school per team (max per team, leftovers):")
    for school, allocation in max_students_per_school.items():
        print(f" - {school}: {allocation}")

    return max_students_per_school

# calculateOptimalDistribution
def calculateOptimalDistribution(total_males, total_females, group_size):
    num_students = 50  # Total number of students per tutorial group
    num_teams = num_students // group_size  # Base number of teams
    remainder = num_students % group_size   # Remainder to distribute as extra

    # Determine number of normal teams (group_size) and remaining larger teams (group_size + 1)
    normalTeams = num_teams - remainder
    remainingTeams = remainder

    #print(f"Creating {normalTeams} teams of {group_size} and {remainingTeams} teams of {group_size + 1}")

    # Initialize variables for gender distribution and remaining counts
    team_gender_template = []
    remaining_males, remaining_females = total_males, total_females

    # Fill larger teams first to spread students more evenly
    for i in range(remainingTeams):
        current_team_size = group_size + 1
        if remaining_males >= remaining_females:
            male_count = min(remaining_males, (current_team_size + 1) // 2)
            female_count = current_team_size - male_count
        else:
            female_count = min(remaining_females, (current_team_size + 1) // 2)
            male_count = current_team_size - female_count

        team_gender_template.append((male_count, female_count))
        remaining_males -= male_count
        remaining_females -= female_count

    # Fill remaining normal-sized teams
    for i in range(normalTeams):
        current_team_size = group_size
        if remaining_males >= remaining_females:
            male_count = min(remaining_males, (current_team_size + 1) // 2)
            female_count = current_team_size - male_count
        else:
            female_count = min(remaining_females, (current_team_size + 1) // 2)
            male_count = current_team_size - female_count

        team_gender_template.append((male_count, female_count))
        remaining_males -= male_count
        remaining_females -= female_count

    # Distribute any leftover students to balance the gender distribution across all teams
    for i in range(len(team_gender_template)):
        if remaining_males == 0 and remaining_females == 0:
            break
        male_count, female_count = team_gender_template[i]

        # Fill remaining males and females to balance across teams
        if remaining_males > 0 and male_count < group_size // 2 + 1:
            male_count += 1
            remaining_males -= 1
        elif remaining_females > 0 and female_count < group_size // 2 + 1:
            female_count += 1
            remaining_females -= 1

        team_gender_template[i] = (male_count, female_count)

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
    # Use schoolChecker to determine max per school per team
    max_per_school = schoolChecker(male_schools, female_schools, group_size)

    groups = []  # Final list of groups

    # Flatten male and female students into lists for easier access
    male_students = [student for students in male_schools.values() for student in students]
    female_students = [student for students in female_schools.values() for student in students]

    # Get the optimal gender distribution per team
    teamGenderTemplate = calculateOptimalDistribution(len(male_students), len(female_students), group_size)
    
    # Initialize counts for schools in each team
    school_counts = {school: 0 for school in max_per_school.keys()}
    
    # Create main groups based on the template
    for male_count, female_count in teamGenderTemplate:
        create_group = []  # Temporary group for the current team
        group_school_counts = {}  # Track school counts in the current group

        # Add the exact number of males specified by `male_count`
        for _ in range(male_count):
            added = False
            for student in male_students:
                school = student['School']
                # Ensure school count for this group doesn’t exceed max constraint
                if group_school_counts.get(school, 0) < max_per_school[school][0] or \
                   (max_per_school[school][1] > 0 and school_counts[school] < group_size + 1):
                    create_group.append(student)
                    male_students.remove(student)
                    group_school_counts[school] = group_school_counts.get(school, 0) + 1
                    school_counts[school] += 1
                    added = True
                    break

            # Relax the constraint if no valid student was found
            if not added:
                if male_students:
                    create_group.append(male_students.pop(0))

        # Add the exact number of females specified by `female_count`
        for _ in range(female_count):
            added = False
            for student in female_students:
                school = student['School']
                # Ensure school count for this group doesn’t exceed max constraint
                if group_school_counts.get(school, 0) < max_per_school[school][0] or \
                   (max_per_school[school][1] > 0 and school_counts[school] < group_size + 1):
                    create_group.append(student)
                    female_students.remove(student)
                    group_school_counts[school] = group_school_counts.get(school, 0) + 1
                    school_counts[school] += 1
                    added = True
                    break

            # Relax the constraint if no valid student was found
            if not added:
                if female_students:
                    create_group.append(female_students.pop(0))

        # Add the completed group to the list of groups
        groups.append(create_group)

    # Distribute any leftover students to avoid single-student groups
    leftovers = male_students + female_students
    for student in leftovers:
        for group in groups:
            if len(group) < group_size + 1:
                group.append(student)
                break

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

        # Uncomment this to only do it for 1 tutorial group
        #break

# Run Algorithm
mainProcess(pathToFile, Students, sortedStudents)
