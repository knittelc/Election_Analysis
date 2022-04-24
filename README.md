# Election_Analysis
## Project Overfiew
A Colorado Board of Elections employee gave the following tasks to complete the elction audit of a recent local congressional election.

1. Calculate the total nubmer of votes cast.
2. Get a complete list of the candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
-Data Source: election_results.csv
-Software: Python 3.9.7, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,771 total votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the votes; 85,213 in total.
    - Diana DeGette received 73.8% of the votes; 272,892 in total.
    - Raymon Anthony Doane received 3.1% of the votes; 11,606 in total.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the votes; 272,892 in total.

## Challenge Overview

This challenge was a good introduction to seeing the capabilities of python, the built in funcions, pulling in a csv file and with the Visual Studio showing the output and writing a to a text file all in the same window.  The amount of computing python was able to accomplish very quickly shows the power of rapidly sifting and compliling out put through this data.

## Challenge Summary
As an initial first step, I did pull the csv file into excel to understand what type of data and set up the file was in and to ascertain if it needed any type of cleaning and to ensure it was not missing key parts.  Then, using the power of python, I loaded the csv file I was given as the data starting point.  Then the rough process for the outcomes were to initialize all of the counted objects (total votes, candidate options, candidate votes). Then, to use computing fuctions to find the winner of the total results.  Then python had to actually read the file.  The data were looped over to find all of the counts per row for total votes, unique candidate names, and then the vote counts attributed to said candidates.  Here is the virst time I learned to write a file to text and seeing how it corresponded to the newly created analysis folder bolstered my confidence that the code was working appropriately.  After all the data were complied, I printed it into a readable form showing the summary above and was able to declare a winner!
