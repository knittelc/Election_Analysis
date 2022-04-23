#Election_Data_Analsis
import csv

# Create a filename variable to a direct or indirect path to the file.
file_to_load = "Resources/election_results.csv"
#Assign variable to save the file to a path
file_to_save = "analysis/election_analysis.txt"

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

#Print each row in the CSV file
for row in file_reader:
    print(row)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Does this change it?")



#1. The total number of votes cast
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4 The total number of votes each candidate won
#5. The winner of the election based on popular vote.


#Close the file.
