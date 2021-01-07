# Add our dependencies
import csv
import os
# Assign a variable for the file to load a file from a path
file_to_load = os.path.join('Resources','election_results.csv')

# Create a filename variable to direct or indirect path to the file.
file_to_save = os.path.join('analysis','election_analysis.txt')

# Open the election results and read the file --with will also close the reading of the file.
with open(file_to_load) as election_data:
    
    # To do: Perform analysis here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read and print header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file
    #for row in file_reader:
     #   print(row)



# Using the with statement to open the file as text file
#with open(file_to_save,'w') as txt_file:
    # Write data to the file
    #txt_file.write('Arapahoe\nDenver\nJefferson')

# Data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote