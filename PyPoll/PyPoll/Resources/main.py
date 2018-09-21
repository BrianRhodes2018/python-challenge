import csv
import os
from decimal import Decimal
i = 0

candidateDict = {}
leadingCandidate = None
leadingVotes = 0

productionfile = "election_data.csv"

with open(productionfile) as csv_file:
   CSVreader = csv.reader(csv_file)

   next(CSVreader)

   for row in CSVreader:
       voterID = row[0]
       county = row[1]
       candidate = row[2]

       #Add candidates to dictionary
       if candidate in candidateDict:
           candidateDict[candidate] += 1
       else:
           candidateDict[candidate] = 1
       #Calculating voter stats
       candidateVotes = candidateDict.get(candidate)
       if candidateVotes > leadingVotes:
           leadingCandidate = candidate
           leadingVotes = candidateVotes

       i += 1

       
f = open("Output.txt" , "w")
f.write
f.write('Election Results/n')
f.write('---------------------------/n')
f.write('Total Votes: ' + str(i))
f.write('/n---------------------------')
for candidate, votes in candidateDict.items():
    f.write(candidate + ': ' + str(round((votes / i) * 100, 3)) + '% (' + str(votes) + ')')
f.write('/n---------------------------')
f.write('/nWinner: ' + leadingCandidate)
f.write('/n---------------------------')



print('Election Results')
print('---------------------------')
print('Total Votes: ' + str(i))
print('---------------------------')
for candidate, votes in candidateDict.items():
    print(candidate + ': ' + str(round((votes / i) * 100, 3)) + '% (' + str(votes) + ')')
print('---------------------------')
print('Winner: ' + leadingCandidate)
print('---------------------------')