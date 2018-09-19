
import csv

def readLines():
    with open('budget_data.csv', 'rU') as data:
        reader = csv.reader(data)
        row = list(reader)
        for x in row:
            for y in x:
                print type(float(y)),
readLines()
