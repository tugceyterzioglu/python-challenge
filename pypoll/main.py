import pandas as pd
from pathlib import Path

# load data from CSV file to pandas dataframe in python
file_path = '/Users/DataBootcamp/python-challenge/PyPoll/resources/election_data.csv'
df = pd.read_csv(file_path)

# total number of votes cast
total_votes_cast = df['Ballot ID'].nunique()

# complete list of candidates who received votes
candidates = df['Candidate'].unique()

# total number of votes each candidate won
votes_won = df['Candidate'].value_counts()

# percentage of votes each candidate won
percentage_of_votes = (votes_won / total_votes_cast) * 100

# winner of election based on popular vote
winner = votes_won.idxmax()

# print the analysis to terminal 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes_cast}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentage_of_votes[candidate]:.3f}% ({votes_won[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# export a text file with the results
election_results_file_path = '/Users/DataBootcamp/python-challenge/PyPoll/analysis/election_results.txt'
with open(election_results_file_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes_cast}\n")
    file.write("-------------------------\n")
    for candidate in candidates:
        file.write(f"{candidate}: {percentage_of_votes[candidate]:.3f}% ({votes_won[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

print(f"\nResults have been saved to election_results.txt.")
