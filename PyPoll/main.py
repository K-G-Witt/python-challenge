# Import required packages:
import os
import csv


# Specify file path for election_data.csv:
election_data_path = os.path.join("Resources", "election_data.csv")


# Generate empty vars and lists to store information needed later:
tot_votes = 0
ballot_ID = []
county = []
candidate_name = []


# Read in election_data.csv as read-write:
with open(election_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Defining the header:
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    # Loop through the dataset, starting after the header row:
    for row in csvreader:

        # Define col1 as containing Ballot ID:
        ballot_ID.append(row[0])

        # Define col2 as containing County:
        county.append(row[1])

        # Define col3 as containing Candidate's Names:
        candidate_name.append(row[2])

        # Calculate total number of votes:
        tot_votes = len(ballot_ID)

        # Create a dictionary to count number of votes per unique candidate:
    votes_by_candidate = {}

    # Count number of votes, per unique candidate
    for votes in candidate_name:
        if votes in votes_by_candidate:
            votes_by_candidate[votes] += 1
        else:
            votes_by_candidate[votes] = 1

    # Select the winner:
    winner = max(votes_by_candidate, key=votes_by_candidate.get)
        
    # Print the analysis to the terminal:
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {tot_votes}")
    print("----------------------------")
    # Prints results by candidate, with each candidate name on a new line:
    for candidate, count in votes_by_candidate.items():
        percentage = (count / tot_votes) * 100
        print(f"{candidate}: {percentage: .3f}% ({count})")   
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

    # Export the analysis, as a .txt file, to the Analysis subfolder:
    election_data_txt = os.path.join("Analysis", "election_data.txt")
    with open(election_data_txt, "w") as outfile:
        outfile.write("Election Results\n")
        outfile.write("----------------------------\n")
        outfile.write(f"Total Votes: {tot_votes}\n")
        outfile.write("----------------------------\n")
        for candidate, count in votes_by_candidate.items():
            percentage = (count / tot_votes) * 100
            outfile.write(f"{candidate}: {percentage: .3f}% ({count})\n")
        outfile.write("----------------------------\n")
        outfile.write(f"Winner: {winner}\n")
        outfile.write("----------------------------\n")    
