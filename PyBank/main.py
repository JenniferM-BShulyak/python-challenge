#PyBank Script

#Import budget_data.csv
import os
import csv  #import csv module
path = os.path.join("Resources", "budget_data.csv")
data = open(path)  #data is now a file object
Reader = csv.reader(data)   #created a reader object to use

header = next(Reader) #The first line is the header

#######################################
#Create Variables 
num_months = 0  #Need to keep track of number of months
net_total_amount = 0    #Track net total amount of profits/losses
#Variables to track increases and decreases in profit
greatest_incr = 0
greatest_incr_month = 0
greatest_decr = 0
greatest_decr_month = 0
first_month = 0
previous_month = 0
#Track changes occuring to find the average
changes = 0
changes_total = 0
num_changes = 0

#########################################
#Read the data using a For Loop
for row in Reader:  #Each row will be a line (row/list) from the CSV file
    num_months += 1 #increment the number of months
    net_total_amount += int(row[1])   #the profit/losses amount is the second value in the row

    #Finding the average in Profit/Losses changes
    if num_months > 1: #Have to skip the first month because it is the starting point
        changes = int(row[1]) - previous_month #store the change since the previous month
        changes_total += changes    #store the total amount that has changed
        num_changes +=1     #keep track of the number of changes

        #Check if current row's proft/losses beat the current greatest increase and decrease titles
        if changes > greatest_incr:     #If this month's increase is the biggest so far
            greatest_incr = changes     #Store as new greatest increasee
            greatest_incr_month = row[0]    #Store the month/year this occurred

        elif changes < greatest_decr:    #If this month's change is the worst so far
            greatest_decr = changes     #Store as the greatest decrease
            greatest_decr_month = row[0]    #Store the month/year this occurred

    
    
    #Set new previous month 
    previous_month = int(row[1])

#Calculate Avereage changes in profit/losses
average_change = round((changes_total / num_changes), 2)


###########################################
#Print Analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_incr_month} ({greatest_incr})")
print(f"Greatest Decrease in Profits: {greatest_decr_month} ({greatest_decr})")


#Write to Analysis 
return_path = "analysis/analysis.txt"
file = open(return_path, 'w')
writer = csv.writer(file)   
writer.writerow(["Financial Analysis"])
writer.writerow(["----------------------------"])
writer.writerow([f"Total Months: {num_months}"])
writer.writerow([f"Total: ${net_total_amount}"])
writer.writerow([f"Average Change: ${average_change}"])
writer.writerow([f"Greatest Increase in Profits: {greatest_incr_month} ({greatest_incr})"])
writer.writerow([f"Greatest Decrease in Profits: {greatest_decr_month} ({greatest_decr})"])