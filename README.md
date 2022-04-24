# Election_Audit
## Project Overview
A Colorado Board of Elections employee gave the following tasks to complete the elction audit of a recent local congressional election.

- Calculate the total nubmer of votes cast.
- Provide a breakdown of the number of votes and percentage of total votes for each county in the precint.
- Print which county had the largest number of votes.
- Get a complete list of the candidates who received votes.
- Calculate the total number of votes each candidate received.
- Calculate the percentage of votes each candidate won.
- Determine the winner of the election based on popular vote.


## Resources
-Data Source: election_results.csv
-Software: Python 3.9.7, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,771 total votes cast in the election.
- The county results were:
   - Jefferson county placed 10.5% of the votes; 38,855 in total.
   - Denver county placed 82.8% of the votes; 306,055 in total.
   - Arapahoe county placed 6.7% of the votes; 24,801 in total.
- Denver had the largest voter turnout thus number of votes
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

![election results txtfile grab](https://user-images.githubusercontent.com/102183530/164994324-dede2ce6-fbae-4508-bf01-90f4ad0eeb5a.png)

###### Text file screen grab of election results and deliverables.

## Challenge Overview

This challenge was a good introduction to seeing the capabilities of python, the built in funcions, pulling in a csv file and with the Visual Studio showing the output and writing a to a text file all in the same window.  The amount of computing python was able to accomplish very quickly shows the power of rapidly sifting and compliling out put through this data.

## Challenge Summary
As an initial first step, I did pull the csv file into excel to understand what type of data and set up the file was in and to ascertain if it needed any type of cleaning and to ensure it was not missing key parts.  Then, using the power of python, I loaded the csv file I was given as the data starting point.  Then the rough process for the outcomes were to initialize all of the counted objects (total votes, candidate options, candidate votes). Then, to use computing fuctions to find the winner of the total results.  Then python had to actually read the file.  The data were looped over to find all of the counts per row for total votes, unique candidate names, and then the vote counts attributed to said candidates.  Here is the virst time I learned to write a file to text and seeing how it corresponded to the newly created analysis folder bolstered my confidence that the code was working appropriately.  After all the data were complied, I printed it into a readable form showing the summary above and was able to declare a winner!

## Election Audit Summary
Per the request of the election commision; a python program was written to audit and verify election results.  Now that the general "shell" of the code exists, all other elections could be run through this code to determine other election outcomes.  The way it is written we could have multiple candidates added, as well as an expansion of counties wiht out any adjusting, making this a very versitile code.

Adjustments would only have to be made based on how the other election data is filed to ensure the correct information is aligning with what I have designed.  For example, if there were more categories input like a "district" at a more local level; the code would just have to be tweaked to get down one more level of data.  I would do this by simply adding another set of variables and align them with the district level.  Political party of candidates could also be added, possibly changing and updating. the rows we are pulling information from.  If we had more granular data we could also use pythons "grouping" method to keep like and like together but give more information to the election commission. 
