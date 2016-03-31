#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

  def read_data(data):
   # COMPLETE THIS FUNCTION

  def get_min_score_difference(self, parsed_data):
    # COMPLETE THIS FUNCTION

  def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION

Answer:
  
  import csv

with open('/Users/stewartstout/desktop/football.csv', 'r') as f:
	reader = csv.reader(f)
	your_list = list(reader)

i = 1

for row in your_list[1:]:
	diff = int(row[5]) - int(row[6])
	your_list[i].append(diff)
	i += 1

r = 2
smallest_difference = ''
min = your_list[r - 1][8]

while r < len(your_list):
	if your_list[r][8] < min:
		smallest_difference = your_list[r][0]
		min = your_list[r][8]
		
	r += 1

print smallest_difference
