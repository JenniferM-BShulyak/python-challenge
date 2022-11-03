#PyPoll Part of python challenge

#Import necessary modules
import os
import csv

path = os.path.join("Resources", "election_data.csv")

with open(path) as file_object:
    body = csv.reader(file_object)
    header = next(body)     #Take header off of body
    
    #Initilize variables
    num_ballots = 0
    candidates = [] #Keep track of candidates
    vote_count = [] #Keep track of votes for each candidate
   
    #Loop through ballots
    for row in body:
        num_ballots += 1

        #check to see if candidate has appeared before
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_count.append(1)
        else:
            vote_count[candidates.index(row[2])] +=1    #Find the index for a candidate and add to their vote count

    #Check vote percentages
    vote_perc = []
    for cand in vote_count:
        vote_perc.append(round(cand/num_ballots*100, 3))

    #Who one the election
    max = max(vote_count)
    index_max = vote_count.index(max)
    winner = candidates[index_max]

    ######################################################

#Print out election results
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {num_ballots}")
    print("----------------------------")
    for x in range(len(candidates)):
        print(f"{candidates[x]}: {vote_perc[x]}% ({vote_count[x]})")

    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

    

#Write to analysis file
    return_path = os.path.join("analysis/analysis.txt")
    file = open(return_path, "w")
    writer = csv.writer(file)
    writer.writerow(["Election Results"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Votes: {num_ballots}"])
    writer.writerow(["----------------------------"])
    for x in range(len(candidates)):
        writer.writerow([f"{candidates[x]}: {vote_perc[x]}% ({vote_count[x]})"])

    writer.writerow(["----------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["----------------------------"])


    

  




    
