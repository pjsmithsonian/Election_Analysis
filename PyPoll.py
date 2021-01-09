# Add our dependencies
import csv
import os
# Assign a variable for the file to load a file from a path
file_to_load = os.path.join('Resources','election_results.csv')

# Create a filename variable to direct or indirect path to the file.
file_to_save = os.path.join('analysis','election_analysis.txt')

# 1. Initialize a total vote counter
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file --with will also close the reading of the file.
with open(file_to_load) as election_data:
    
    # To do: Perform analysis here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
    # Add to total vote count
        total_votes += 1

        # Get candidate name from each row
        candidate_name = row[2]

        # If candidate does not match existing candidate...
        # dd the candidate to the candidate list
        if candidate_name not in candidate_options:
            # Add to list of candidates.
            candidate_options.append(candidate_name)   

            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0 

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1 

# Save the results to our txt file
with open(file_to_save,'w') as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n"
    )
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    # Determine the percentage of votes for each candidate by looping through the counts.
    # iterate throught candidate list
    for candidate_name in candidate_votes:
        # retrieve vote count of candidate
        votes = candidate_votes[candidate_name]

        # calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}%  ({votes:,})")
        print(candidate_results)

        # save the candidate results to our txt file
        txt_file.write(candidate_results + "\n")

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percent = vote_percent
            winning_count = votes
            winning_percentage = vote_percentage
            # and set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
            winning_candidate_summary = (
                f"---------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"---------------------------\n"
            )
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)