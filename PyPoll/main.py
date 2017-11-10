import csv

file = 'election_data_2.csv'

#first create dictionary where key is candidate, value is number of votes
tally = {}

#open the file in read mode and store the data in tally in the form {candidate : number_of_votes}
with open(file, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	first_row = next(csvreader)
	for row in csvreader:
		if row[2] in tally:
			tally[row[2]] += 1
		else:
			tally[row[2]] = 1


#initialize total number of votes and the winner of the election; the for loop finds the desired result
total_votes = 0
winner = ''

for cand in tally:
	total_votes += tally[cand]
	if winner not in tally:
		winner = cand
	else:
		if tally[cand] > tally[winner]:
			winner = cand


#Print out the election results to the terminal
print("Election Results")
print("______________________")
print("Total votes: %d"%(total_votes))
print("______________________")
for cand in tally:
	print(cand + ": " + str(round(100.0 * float(tally[cand])/float(total_votes),2)) + "%" + "     " + "(" + str(tally[cand]) + ")" )
	#print("%s: %f   (%d)"%(cand, round(100.0 * float(tally[cand])/float(total_votes),2), tally[cand]   ) )
print("______________________")
print("Winner: " + winner)
print("______________________")


#Write the election results to a file
with open('output.txt', 'w') as f:
	f.flush()
	f.write("Election Results" + "\n")
	f.write("______________________" + "\n")
	f.write("Total votes: %d"%(total_votes) + "\n")
	print("______________________")
	for cand in tally:
		f.write(cand + ": " + str(round(100.0 * float(tally[cand])/float(total_votes),2)) + "%" + "     " + "(" + str(tally[cand]) + ")" + "\n" )
		#print("%s: %f   (%d)"%(cand, round(100.0 * float(tally[cand])/float(total_votes),2), tally[cand]   ) )
	f.write("______________________" + "\n")
	f.write("Winner: " + winner + "\n")
	f.write("______________________" +  "\n")
