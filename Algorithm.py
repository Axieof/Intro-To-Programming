# Intro to computational thinking
# Assignment 1
# Team 3
# Tham, Nisha, Jerdel, Boris, Pritheev

# Imports
import csv

tutorialList = []
indexList = []
schoolList = []
nameList = []
genderList = []
gpaList = []

with open('../records.csv', mode='r') as recordsCSV:
    records = csv.reader(recordsCSV)
    for line in records:
        tutorialList.append(line[0])
        indexList.append(line[1])
        schoolList.append(line[2])
        nameList.append(line[3])
        genderList.append(line[4])
        gpaList.append(line[5])

print(nameList)

