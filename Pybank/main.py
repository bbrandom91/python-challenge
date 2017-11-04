import csv
#First thing we need is the file to open; let the user input it or hard code?
file = 'budget_data_1.csv'
num_months = 0
data = []


#Now let's open the file in read mode

with open(file, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	first_row = next(csvreader)
	for row in csvreader:
		s = row
		s[1] = float(s[1])
		data.append(s)

def get_total(x):
	value = 0.0
	for j in x:
		value += j[1]
	return value
def get_avg(x):
	value = 0.0
	for j in x:
		value += j[1]
	value = round(value/len(x))
	return value
def get_max(x):
	value = x[0]
	for j in range(1,len(x)):
		if x[j][1] > value[1]:
			value = x[j]
	return value
def get_min(x):
	value = x[0]
	for j in range(1,len(x)):
		if x[j][1] < value[1]:
			value = x[j]
	return value



print("Financial Analysis")
print("________________________")
print("Total Months: %d"%(len(data)))
print("Total Revenue: $%d"%(get_total(data)))
print("Average Revenue Change: $%d"%(get_avg(data)))
print("Greatest Increase in Revenue: %s ($%d)"%(get_max(data)[0],get_max(data)[1]))
print("Greatest Decrease in Revenue: %s ($%d)"%(get_min(data)[0],get_min(data)[1]))

with open('output.txt', 'w') as f:
	f.flush()
	f.write("Financial Analysis" + "\n")
	f.write("________________________" + "\n")
	f.write("Total Months: %d"%(len(data)) + "\n")
	f.write("Total Revenue: $%d"%(get_total(data)) + "\n")
	f.write("Average Revenue Change: $%d"%(get_avg(data)) + "\n")
	f.write("Greatest Increase in Revenue: %s ($%d)"%(get_max(data)[0],get_max(data)[1]) + "\n")
	f.write("Greatest Decrease in Revenue: %s ($%d)"%(get_min(data)[0],get_min(data)[1]) + "\n")





