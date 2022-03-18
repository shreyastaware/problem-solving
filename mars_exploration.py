#!/bin/python3

# 19 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-mars-exploration/problem

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    num_of_characters_changed = 0
    LEN = len(s)
    
    for i in range(0, LEN, 3):
        if s[i] != 'S':
            num_of_characters_changed += 1
            
        if s[i+1] != 'O':
            num_of_characters_changed += 1
        
        if s[i+2] != 'S':
            num_of_characters_changed += 1
        
        # num_of_characters_changed += sum((s[i] != 'S', s[i+1] != 'O', s[i+2] != 'S'))
    
    return num_of_characters_changed
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
