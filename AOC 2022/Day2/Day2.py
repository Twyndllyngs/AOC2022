# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 00:26:57 2022

@author: Rohan Aby P
"""

import numpy as np
import pandas as pd

file1 = open("Input_P2.txt",'r')
lines = file1.readlines()

score=0

"""
# Part 1 strategy
for i in range(0,len(lines)):
    arr = lines[i].split()
    
    if arr[1]=='X' and arr[0]=='A':
        score += 1+3
    elif arr[1]=='X' and arr[0]=='B':
        score += 1+0
    elif arr[1]=='X' and arr[0]=='C':
        score += 1+6
        
    elif arr[1]=='Y' and arr[0]=='A':
        score += 2+6
    elif arr[1]=='Y' and arr[0]=='B':
        score += 2+3
    elif arr[1]=='Y' and arr[0]=='C':
        score += 2+0
        
    elif arr[1]=='Z' and arr[0]=='A':
        score += 3+0
    elif arr[1]=='Z' and arr[0]=='B':
        score += 3+6
    elif arr[1]=='Z' and arr[0]=='C':
        score += 3+3
    else:
        print("Error")
"""        
        
# Part 2 strategy        
        
for i in range(0,len(lines)):
    arr = lines[i].split()
    
    if arr[0]=='A' and arr[1]=='X':
        score += 0+3
    elif arr[0]=='A' and arr[1]=='Y':
        score += 3+1
    elif arr[0]=='A' and arr[1]=='Z':
        score += 6+2

    elif arr[0]=='B' and arr[1]=='X':
        score += 0+1
    elif arr[0]=='B' and arr[1]=='Y':
        score += 3+2
    elif arr[0]=='B' and arr[1]=='Z':
        score += 6+3

    elif arr[0]=='C' and arr[1]=='X':
        score += 0+2
    elif arr[0]=='C' and arr[1]=='Y':
        score += 3+3
    elif arr[0]=='C' and arr[1]=='Z':
        score += 6+1

print(score)        
    