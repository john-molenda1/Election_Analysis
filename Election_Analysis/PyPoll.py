# FIGURE OUT HOW TO COMMIT USING GIT BASH

# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Election_Analysis", "analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

#Initailize candidate options and votes
candidate_options = []

# Declare empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_date = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
   
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add votes to candidates 
        candidate_votes[candidate_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote total
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the canddidate name and percentage of the votes
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    
        # To do: print out each candidate's name, vote count, and percentage of 
        # votes to the terminal

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        # Print out each candidate's name, vote count, and percentage of votes to the terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine the winning candidate
        winning_candidate_summary = (
            f"----------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"----------------------\n"
        )
print(winning_candidate_summary)
# Save the winning candidate's results to the text file.
txt_file.write(winning_candidate_summary)

# Print the candidate list
# print(candidate_votes)

# Print the total votes.
# print(total_votes)

# Close the file.
election_data.close()
    # If you don't close the file, you can lose some of the data

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()


