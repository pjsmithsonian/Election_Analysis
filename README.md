# Election_Analysis

## Project overview
A Colorado Board of Elections employee has gave the tasks below to complete an election audit of a recent congressional election.

1. Calculate total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code

## Summary

![Results](/Resources/election_results.PNG)

The election analysis shows:

- Total Votes: 369,711
- The Candidates Were:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
- The Candidate Results Were:	
	- Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
	- Diana DeGette received 73.8% of the vote and 272,892 number of votes.
	- Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The Winner of the Election was:
	- Candidate Diana DeGette who received 73.8% of the vote and 272,892 number of votes.
	
## Challenge Overview
### Election-Audit Overview
The purpose of this audit was automate a way to determine the total number of votes received, determine the candidates receiving votes, and ultimately determine a winner. Also, we want to make this process such that it could be exteneded to other elections in the future and be easily modified.

### Election-Audit Results

- Total Votes: 369,711
- Votes by County:
	- Jefferson: 10.5% or 38,855 votes
	- Denver: 82.8% or 306,055 votes
	- Arapahoe: 6.7% or 24,801 votes
- Denver had the most votes of all counties with 306,055
- The Candidate Results Were:	
	- Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
	- Diana DeGette received 73.8% of the vote and 272,892 number of votes.
	- Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The Winner of the Election was:
	- Candidate Diana DeGette who received 73.8% of the vote and 272,892 number of votes.

## Challenge Summary
	
### Election-Audit Summary	
Using Python to generate these results will allow you to make this analysis easier for other elections. This could be accomplished by updating the election_results.csv file which serves as the data source, while keeping the formatting the same. Because our script will dynamically take in all the names of candidates and count the votes, this can determine the winners for almost any election.

Changes that can be made to this script for future elections could include doing the analysis based off of city if that were included in the election_results.csv instead of County. We could also, with a few edits, determine the votes for each candidate by county. Again, this would require a little more work, but could provide additional insights that may be helpful to the Board of Elections.

