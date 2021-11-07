# Election_Analysis

## Election Audit Overview
The purpose for the election audit is to provide Seth and Tom the necessary data to provide the election commission. Specifically, they want to know the total number of votes cast in each county, what percentage of votes were cast by each county, and which county had the highest turnout. On top of that they obviously need to know who won the election, how many votes were cast for each candidate, and what percentage of the total vote was garnered by each individual.

## Election Audit Results
### County Vote Breakdown
*How many votes were cast in this congressional election? - Total Voter Turnout: 369,711
![image](https://user-images.githubusercontent.com/92773195/140629302-fe23cb4f-1f0d-4d8a-9dbc-84e0e3a67531.png)
  
*Voter Analyis By County
  Jefferson County achieved 10.5% of the total votes cast with 38,855
  Arapahoe County had the smallest total turnout with only 6.7% of the total votes with a mere 24,801 votes
  Denver dominated the election with a shocking 82.8% of the total votes cast with a whopping 306,055 total votes
![image](https://user-images.githubusercontent.com/92773195/140629410-b153e174-12e6-4c4a-b93c-91d2ea9f546e.png)
*Which County had the most votes cast?
Denver 
![image](https://user-images.githubusercontent.com/92773195/140629430-eda0b1a0-2882-4c6d-bbef-5ddca5a5b535.png)
### Candidate Vote Breakdown
* Charles Casper Stockham received just shy of a quarter of the total votes cast with 85,213 - resulting in 23% of votes cast for him
* Diana DeGette, on the flip side, received 272,892 out of the total 369,711 votes cast - meaning that 73.8% of voters cast a vote for Diana
* Raymon Anthony Doane barely registered any votes himself with only 3.1% of the voters selecting Raymon - a total of 11,606 votes 
* ![image](https://user-images.githubusercontent.com/92773195/140629527-41673685-385d-46c6-a205-7445a57e33cc.png)

### Who won the election?
Congratulations to Diana DeGette on winning a landslide election with 73.8% of all votes going to her and 272,892 of the votes!!!!
![image](https://user-images.githubusercontent.com/92773195/140629530-107cc2d1-53bf-431e-8bd5-850dcbdf3fef.png)

## Election-Audit Summary
To all the esteemed members of the election commission, this script can be used, with some minor alterations, for any election in the future for auditing purposes. The only things that would need to be changed are the .csv and .txt files at the very beginning that are being used to read the data and output the results. However, please ensure to use the same column headers and order for reading the csv data.

### Potential Modifications For Improvement
1) The code could easily be modified to include how each county voted for each candidate, their total number of votes garnered, and the percentage they received. This could be done in the same manner that we created the county and candidate results, only by doing it for each individual county.
2) If you wanted to understand where voter turnout may be an issue, you can use the same code that was used to create the "largest_county_turnout" to determine which had the smallest county turnout. It may also be beneficial to add total 18+ aged residents in each county, and number of registered voters, to see how the voter turnout is doing in each county relative to the total possible number of people that could vote. 
