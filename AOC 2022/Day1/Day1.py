# -*- coding: utf-8 -*-
"""
Day 1 of AOC 2022
"""

import numpy as np
import pandas as pd

file1 = open("Input_P1.txt",'r')
lines = file1.readlines()

cal = []
cal_sum = 0

for i in range(0,len(lines)):   #reads along the entire list
    line = lines[i].strip()     #removes the extra spaces
    #print(line)
    if line.isnumeric():        #checks for null cases or alphabets
        #print(line)
        cal_sum+=int(line)      #change to int cz it's a string
        if i==len(lines)-1:
            cal.append(cal_sum) #for last array cz edge case

    else:
        #print(i)
        cal.append(cal_sum)     #appending list recommended than dynamic arrays
        cal_sum=0

sort_cal = np.sort(cal)         #bubble sort go brrr
cal_flip = np.flip(sort_cal)    #biggest first

print(cal_flip[0])
print(cal_flip[1])
print(cal_flip[2])


print(cal_flip[0]+cal_flip[1]+cal_flip[2])      
   
    
    













