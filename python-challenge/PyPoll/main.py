import csv
import os

# 1: Load the data
data_path = r'C:\Users\devin\OneDrive\Desktop\python-challenge\PyPoll\Resources\election_data.csv'

# 2: Initialize variables
total_votes = 0
candidate_votes = {}        # This is not a list, but a dictionary so {} is used instead of []. // Dictionaries are used when one type of data needs to be associated with another (i.e candidate names & vote counts).

# 3: Read the CSV file
with open(data_path, 'r') as file:
    reader = csv.DictReader(file)       # csv.DictReader reads the first row for keys, which provides the keys for the dictionaries. It also parses subsequent rows into dictionaries.
    for row in reader:
        total_votes += 1
        candidate = row['Candidate']        #To find the name of the candidate in the row.
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1     # Inidcates that if the candidate name is already counted, the vote is added to the candidate's existing count.
        else:
            candidate_votes[candidate] = 1      # If the candidate has not received any votes yet, it will give the candidate one vote.

# 4: Calculate percentages and determine the winner
vote_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}     # {} because it is a dictionary, 'candidate' is the key.
winner = max(candidate_votes, key=candidate_votes.get)      # 'max' finds the largest item in an iterable (candidate names), '.get' retrieves values (vote counts) from a dictionary.

# 5: Print results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():        # .items() provieds a way to iterate through both keys and values at the same time.
    print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({votes})")     # .3f formats number to 3 decimal places.  // Candidate, their percentage of votes, and total votes.
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# 6: Export results to a text file
output_folder = r'C:\Users\devin\OneDrive\Desktop\python-challenge\PyPoll\analysis'

# 7: Ensure folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 8: Construct full output path
output_path = os.path.join(output_folder, 'election_results.txt')

# 9: Write to the text file
with open(output_path, 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        txt_file.write(f"{candidate}: {vote_percentages[candidate]:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")

