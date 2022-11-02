#Import budget_data.csv
import csv  #import csv module
path = "Resources/budget_data.csv"
data = open(path)  #data is now a file object
Reader = csv.reader(data)   #created a reader object to use

header = next(Reader) #The first line is the header

num = 0

for row in Reader:
    num = num + 1
    #print(int(row[1]))


print(num)