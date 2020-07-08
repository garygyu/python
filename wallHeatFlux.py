#! /usr/bin/env python
import glob, os
import matplotlib.pyplot as plt
import numpy as np
import csv

def format(value):
    return "%.3f" % value
os.chdir("./")

def get_str(line):
##    print(line)
    str_line = ""
    n = 0
    for element in line:
        if n == 0:
            str_line = str(element)
        else:
            str_line = str_line + "\t" + str(element)
        n += 1
##    print(str_line)
    return str_line

def get_number(line):
    number_line = []
##    print(line)
    n = 0
    for element in line:
        if n ==0:
            number_line.append(float(element))
        else:
            number_line.append(float(element) + 1)
        n += 1
##    print(number_line)
    return number_line

#files = []
##os.chdir("./")
##for file in glob.glob("WallHeatFlux*"):
#for file in os.listdir("./"):
#	if file.startswith("WallHeatFlux"):
#    	##print(file)
#		files.append(file)
#print(files)

##rows = ['2 43 78', '98 12']
##total_sum = total_len = 0
##for row in rows:
##    values = list(map(float, row.split()))
##    total_sum += sum(values)
##    total_len += len(values)
##print(total_sum/total_len)

def subtractTwoLists(list1, list2):
	difference = []
	zip_obj = zip(list1, list2)
	for list1_i, list2_i in zip_obj:
		difference.append(list1_i - list2_i)
	return difference

def addTwoLists(list1, list2):
	sums = []
	zip_obj = zip(list1, list2)
	for list1_i, list2_i in zip_obj:
		sums.append(list1_i + list2_i)
	return sums

files = []
##os.chdir("./")
##for file in glob.glob("WallHeatFlux*"):
for file in os.listdir("./"):
	if file.startswith("sample"):
    	##print(file)
		files.append(file)
print(files)

#ax = plt.subplot(111)
fig, ax = plt.subplots()
legends = ['average',files]

total_x = []
total_y = []
n = 0
for file in files:
	f = open(file, 'r')
	rows = f.readlines()
	f.close()
	if n == 0:
		for row in rows:	
			row = row.strip("\n")
			row = row.split("\t")
			total_x.append(float(row[0]))
			total_y.append(float(row[1]))
	else:
		x = []
		y = []
		for row in rows:	
			row = row.strip("\n")
			row = row.split("\t")
			x.append(float(row[0]))
			y.append(float(row[1]))
		total_x = addTwoLists(total_x, x)
		total_y = addTwoLists(total_y, y)
	n += 1
##print('n = ', n)
##print(len(files))		
averagd_x = [element/float(n) for element in total_x]
averagd_y = [element/float(n) for element in total_y]

print(averagd_x, "\n", averagd_y)

#list1 = [2, 2, 2]
#list2 = [1, 1, 1]
#print(addTwoLists(list1, list2))
ax.plot(averagd_x, averagd_y)

for file in files:	
	f = open(file, 'r')
	rows = f.readlines()
	##print(rows)
	f.close()

	x = []
	y = []        
	for row in rows:
		row = row.strip("\n")
		row = row.split("\t")
		x.append(float(row[0]))
		y.append(float(row[1]))

	##plt.plot(x,y, label='Loaded from dummy file!')
	##ax.plot(x,y)
	
	ax.scatter(x, y, s=1)
	#plt.xlim (0, 0.008)
	#plt.ylim (-5000, 45000)
	#plt.xlabel('distance from onset (m)')
	#plt.ylabel('wall heat flux (W/m^2/K)')
	#plt.title('')

#plt.legend(legends, loc=0, prop={'size': 12})
plt.show()

