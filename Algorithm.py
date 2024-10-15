# Intro to computational thinking
# Assignment 1
# Team 3
# Tham, Nisha, Jerdel, Boris, Pritheev

# Imports
import csv

with open('records.csv', mode='r') as recordsCSV:
    records = csv.reader(recordsCSV)
    for line in records:
        print(line)