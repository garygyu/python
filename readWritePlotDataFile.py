#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import csv

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

def format(value):
    return "%.3f" % value

##f = open("sample.txt")
##lines = f.readlines()
##print(lines)
##f.close()

##f = open("sample_converted.txt", "w+")
##for line in lines:
##    line = line.strip("\n")
##    line = line.split("\t")      
####    print(line)
####    print(len(line))
##    number_line = get_number(line)
##    str_line = get_str(number_line)
##    f.write(str_line + "\n")
####    print(number_line)
####    formatted = [format(v) for v in number_line]
####    f.write(str(formatted) + "\n")
##f.close()

x = []
y = []

####with open('sample_converted.txt','r') as csvfile:
####    plots = csv.reader(csvfile, delimiter=',')
####    print(plots)

##f = open('sample_converted.txt','r')
f = open("sample.txt",'r')
rows = f.readlines()
##print(rows)
f.close()

##legends = [" ", "CFD ","CH2 ","CH3 ","CH4 "]
legends = ["CFD"]        
for row in rows:
    row = row.strip("\n")
    row = row.split("\t")
    x.append(float(row[0]))
    y.append(float(row[1]))

##plt.plot(x,y, label='Loaded from dummy file!')
plt.plot(x,y)
plt.xlabel('distance from onset (m)')
plt.ylabel('wall heat flux (W/m^2/K)')
plt.title('')
plt.legend(legends)
plt.show()
