#Import modules os and csv.
import os
import csv

#set the path for the CSV PyPoll\Resources\election_data.csv

PyPollcsv=os.path.join("PyPoll","Resources","election_data.csv")

#Create the list to store data
total_votes=0

#empty dictionary to catch votes
votes_per_candidates={}

#Open CSV using the relative path
with open(PyPollcsv, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)
    
    print(f"Header:{csv_header}")
    #This print the header columm
    
    #Count the total number of votes
    for row in csvreader:
        total_votes=total_votes+1
        if row[2] not in votes_per_candidates:
            votes_per_candidates[row[2]]=1
        else:
            votes_per_candidates[row[2]]+=1

       
       
       
print("-------------------------------------------------")
print("Election Results")
print("-------------------------------------------------")
print(f"Total Votes:  {total_votes}")
print(f"------------------------------------------------")
#get the results of candidates and percent and total of votes
for candidate, votes in votes_per_candidates.items():
    print(candidate+":"+"{:.3%}".format(votes/total_votes)+"("+str(votes)+")")
print("-------------------------------------------------")
#get the winner name
winner=max(votes_per_candidates, key=votes_per_candidates.get)
print(f"Winner:  {winner}")
print("-------------------------------------------------")


#now create the file.txt for the results of election

f=open("election_results.txt", "w")

f.write("-------------------------------------------------\n")
f.write("Election Results\n")
f.write("-------------------------------------------------\n")
f.write(f"Total Votes:  {total_votes}\n")
f.write(f"------------------------------------------------\n")
for candidate, votes in votes_per_candidates.items():
    f.write(candidate+":"+"{:.3%}".format(votes/total_votes)+"("+str(votes)+")\n")
f.write("-------------------------------------------------\n")
winner=max(votes_per_candidates, key=votes_per_candidates.get)
f.write(f"Winner:  {winner}\n")
f.write("-------------------------------------------------\n")

