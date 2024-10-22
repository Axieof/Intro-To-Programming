# Intro to computational thinking
# Assignment 1
# Team 3
# Tham, Nisha, Jerdel, Boris, Pritheev

# Imports
import csv

# Variable Initialising
tutorialList = []
indexList = []
schoolList = []
nameList = []
genderList = []
gpaList = []
Students = []

# loadData - Reading raw csv data
def loadData(filename, Students):
    with open('records.csv', mode='r') as recordsCSV:
        records = csv.DictReader(recordsCSV)
        for line in records:
            student = {
                'Tutorial Group': line['Tutorial Group'],
                'Student': line['Student ID'],
                'School': line['School'],
                'Name': line['Name'],
                'Gender': line['Gender'],
                'CGPA': line['CGPA']
            }
            Students.append(student)

Students = loadData('records.csv', Students)

# sortStudents - 

# mainProcess

# genderSplit

# schoolAffiliation

# currentCGPA

# exportData

