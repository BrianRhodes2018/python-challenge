
import csv
import os

#Importing the data

with open('budget_data.csv') as csv_file:
   CSVreader = csv.reader(csv_file)
   
#Skipping the header
   
   next(CSVreader)

#Defining variables
   dates = []
   finance = []
   countMonth = 0
   aggregate = 0
   total = 0
   avgDiff = 0
   avgMarker = 0
   totalDiff = 0
   i = 0
   increase1 = 0
   decrease1 = 0
   a = 0


   for row in CSVreader:

       date = row[0]
       finance = row[1]
       total = int(finance,10)
       
       #Skipping the first line of data to find the average

       while i < 1:
            avgMarker = total            
            i += 1
       
       countMonth += 1    
       totalDiff += (total - avgMarker)
      
       avgMarker = total
       
       avgDiff = totalDiff / countMonth
       aggregate += total

# Greatest increase in profits
       if total > increase1:
           increase2 = total
           increase1 = increase2
           increaseDate = date

# Greatest decrease in profits
       if total < decrease1:
           decrease2 = total
           decrease1 = decrease2
           decreaseDate = date

           
f = open("Output.txt" , "w")
f.write('Financial Analysis' + "\n")
f.write('-----------------------------------------\n')
f.write("Total Months: " + str(countMonth) + "\n")
f.write('Total: ' + str(aggregate) + "\n")
f.write('Average Change: $' + str(avgDiff) + "\n")
f.write('Greatest Increase in Profits: ' + str(increaseDate) + ' $'+ str(increase1) + "\n")
f.write('Greatest Decrease in Profits: ' + str(decreaseDate) + ' $'+ str(decrease1) + "\n")
f.close()


print('Financial Analysis')
print('-----------------------------------------')
print("Total Months: " + str(countMonth))
print('Total: ' + str(aggregate))
print('Average Change: $' + str(avgDiff))
print('Greatest Increase in Profits: ' + str(increaseDate) + ' $'+ str(increase1))
print('Greatest Decrease in Profits: ' + str(decreaseDate) + ' $'+ str(decrease1))


