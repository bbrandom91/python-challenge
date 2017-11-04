#first create dictionary where key is candidate, value is number of votes
import csv

file = 'election_data_2.csv'
tally = {}

with open(file, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	first_row = next(csvreader)
	for row in csvreader:
		if row[2] in tally:
			tally[row[2]] += 1
		else:
			tally[row[2]] = 1

def get_total(x):
	value = 0
	for j in x:
		value += x[j]
	return value
def get_winner(x):
	winner = ''
	for cand in x:
		if winner not in x:
			winner = cand
		else:
			if x[cand] > x[winner]:
				winner = cand
	return winner
winner = get_winner(tally) 
total_votes = get_total(tally)


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
