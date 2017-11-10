import csv
#First thing we need is the file to open; let the user input it or hard code?
file = 'budget_data_1.csv'

#Initialize an empty list where we will store the data from the file
data = []


#Open the file in read mode and store the contents in data
with open(file, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	first_row = next(csvreader)
	for row in csvreader:		
		row[1] = float(row[1]) #need to convert data in revenue column to a number
		data.append(row)

#Initialize variables which will store values of interest
total_rev = 0 #total revenue
avg_rev = 0 #average monthly revenue; should this be average of difference from previous month? Then avg_rev ~ rev_final - rev_initial
num_months = len(data) #number of months
min_month = data[0][0] #month with lowest revenue
max_month = data[0][0] #month with highest revenue
diff_min = data[0][1] #revenue of month with lowest revenue
diff_max = data[0][1] #revenue of month with highest revenue

#this for loop calculates total revenue, average revenue, and min and max months and revenue
for rev in data:
	total_rev += rev[1]
	avg_rev += rev[1]/num_months
	if rev[1] < diff_min:
		min_month = rev[0]
		diff_min = rev[1]
	if rev[1] > diff_max:
		max_month = rev[0]
		diff_max = rev[1]



#Printing to the terminal
print("Financial Analysis")
print("________________________")
print("Total Months: %d"%(num_months))
print("Total Revenue: $%d"%(total_rev))
print("Average Revenue Change: $%d"%(avg_rev))
print("Greatest Increase in Revenue: %s ($%d)"%(max_month,diff_max))
print("Greatest Decrease in Revenue: %s ($%d)"%(min_month,diff_min))

#writing to a file
with open('output.txt', 'w') as f:
	f.flush()
	f.write("Financial Analysis" + "\n")
	f.write("________________________" + "\n")
	f.write("Total Months: %d"%(num_months) + "\n")
	f.write("Total Revenue: $%d"%(total_rev) + "\n")
	f.write("Average Revenue Change: $%d"%(avg_rev) + "\n")
	f.write("Greatest Increase in Revenue: %s ($%d)"%(max_month, diff_max) + "\n")
	f.write("Greatest Decrease in Revenue: %s ($%d)"%(min_month, diff_min) + "\n")





