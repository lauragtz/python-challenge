#dataset composed of: Voter ID, County, & Candidate
#total number of votes cast
#complete list of candidates who received votes
#the percentage of votes each candidate won
#the winner of the election based on popular vote

#import os module to create file paths across operating systems
import os

#module for reading CSV files
import csv

#load files
election_data_csv = os.path.join("Resources", "election_data.csv")

#variables
vote = []
county = []
candidate = []
khan = []
correy = []
li = []
o_tooley = []

#lists - delete code // some will not be used
vote_count = []
vote_percentage = []
candidate_list = []
candidate = []
all_candidates = []

#open & create a new header row
with open(election_data_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #read the header row first
    csv_reader = next(csv_file)

    #print(f"CSV Header: {csv_header}")

#total number of votes cast
#voter ID -> county -> candidates
for row in csv_reader:
    vote.append(int(row[0]))
    county.append(row[1])
    candidate.append(row[2])

#total_votes
total_votes = (len(vote))

#complete list of candidates who received votes
#loop
for candidate in all_candidate:
    if candidate == "Correy":
        correy.append(candidate)
        correy_votes = len(correy)
    elif candidate == "Khan":
        khan.append(candidate)
        khan_votes = len(khan)
    elif candidate == "Li":
        li.append(candidate)
        li_votes = len(li)
    elif candidate == "O'Tooley":
        o_tooley.append(candidate)
        o_tooley_votes = len(o_tooley)
#no print

#the percentage of votes each candidate won
khan_percent = round(((khan_votes / total_votes) * 100), 2)
correy_percent = round(((correy_votes / total_votes) * 100), 2)
li_percent = round(((li_votes / total_votes) * 100), 2)
o_tooley_percent = round(((o_tooley_votes / total_votes) * 100), 2)
#noprint

#the winner of the election based on popular vote
#did not want to copy code from classmate; left blank instead
#did not have a source to follow than classmate


#print results
print("Election Results")
print("--------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("---------------------")
print(f"{votes_per_candidate}: {first}% ({votes_per_candidate})")
print(f"{votes_per_candidate}: {second}% ({votes_per_candidate})")
print(f"{votes_per_candidate}: {third}% ({votes_per_candidate})")
print(f"{votes_per_candidate}: {fourth}% ({votes_per_candidate})")
print("-------------------")
print(f"Winner:  {votes_per_candidate}")
print("--------------------")
