# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 00:58:37 2022

@author: Rohan Aby P
"""

import numpy as np
import pandas as pd

file1 = open("Input_P3.txt",'r')
lines = file1.readlines()

'''

# Part 1

score = 0

for i in range(0,len(lines)):   #reads along the entire list
#for i in range(5,6):   #reads along the entire list
    if i<len(lines)-1:
        line=lines[i]
        split = int((len(line)-1)/2)
    else:
        line=lines[i]
        split = int(len(line)/2)
    #print(split)
    
    bag = []
    
    for letter in line:
        bag.append(letter)
    #print(bag)
    
    repeater = 0
    
    for j in range(0,split):
        for k in range(split,len(line)-1):
            #print(bag[j]," ",bag[k])
            if bag[j]==bag[k]:
                #print(bag[j])
                if 97<=ord(bag[j])<=122:
                    score += (ord(bag[j])-96)
                elif 65<=ord(bag[j])<=90:
                    score += (ord(bag[j])-38)
                repeater = 1
            if repeater == 1:
                break
        if repeater == 1:
            break

print(score)

'''


# Part 2

groups = int(len(lines)/3)
priority = 0

for i in range(0,groups):
#for i in range(0,1):
    
    repeater = 0
    
    e1 = lines[(0+(3*i))]
    e2 = lines[(1+(3*i))]
    e3 = lines[(2+(3*i))]
    
    for j in range(0,len(e1)):
        for k in range(0,len(e2)):
            for l in range(0,len(e3)):
                if e1[j]==e2[k] and e1[j]==e3[l]:
                    if 97<=ord(e1[j])<=122:
                        priority += (ord(e1[j])-96)
                    elif 65<=ord(e1[j])<=90:
                        priority += (ord(e1[j])-38)
                    #print(e1[j])
                    repeater = 1
                if repeater == 1:
                    break
            if repeater == 1:
                break
        if repeater == 1:
            break

print(priority)