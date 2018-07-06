"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople = []
melons_sold = []



f = open("sales-report.txt")
for line in f:
    line = line.rstrip() # removes the \n newline character
    entries = line.split("|") # turns each line into a list, so we can use the data
    salesperson = entries[0] # adds their name, the first index it to salesperson variable
    melons = int(entries[2]) # adds number of melons to melon variable

    if salesperson in salespeople: #checks if the name has been added to the list sales person
        position = salespeople.index(salesperson) #creates a variable to get the index of the salesperson
        melons_sold[position] += melons #adds the sale to their melons sold tally at the corresponding index in a seperate list
    else: 
        salespeople.append(salesperson) #if there's no entry yet in salespeople, create one
        melons_sold.append(melons) # adds the melons sold to the list melons


#for i in range(len(salespeople)):
#    print("{} sold {} melons".format(salespeople[i], melons_sold[i]))

def import_file_as_dict(filename):
	print("Iamapotato")
	dic = {}
	f = open(filename, "r")
	for line in f:
		line = line.rstrip().split("|")
		name = line[0]
		sales_melons = [float(x) for x in line[1:]]
#		dic[name] = dic.get(name,[0,0])
		dic[name] = [round((x + y),2) for x , y in zip(dic.get(name,[0,0]),sales_melons)]

#		for orig_sales,orig_melons in dic.get[name,[0,0]:

		#dictionary[name][1] = dictionary.get[name,[]] + 

	return dic



sales_report = import_file_as_dict("sales-report.txt")

for i in sorted(sales_report.keys()):
	print (i)