# 19 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    # D = -1
    # U = +1
    sea_level = 0
    
    path_num = [int(char) for char in path.replace('D', '3').replace('U', '1')]
    
    # print(path_num)
    
    for i in range(steps):
        if path_num[i] == 3:
            path_num[i] = -1
            
    print(path_num)
        
    consec_lis = []
    
    for val in path_num:
        sea_level += val
        consec_lis.append(sea_level)
        
    print(consec_lis)
    
    
    num_valleys = 0
    for i in range(0, steps-1):
        if (consec_lis[i], consec_lis[i+1]) == (0, -1):
            num_valleys += 0.5
        elif (consec_lis[i], consec_lis[i+1]) == (-1, 0):
            num_valleys += 0.5
        
        if consec_lis[0] == -1 and i == 0:
            num_valleys += 0.5
    """ 
    
    num_valleys = 0
    if consec_lis[0] == -1:
        consec_lis.insert(0, 0)
    for i in range(0, len(consec_lis)-1):
        if ( ((consec_lis[i], consec_lis[i+1]) == (0, -1)) or 
             ((consec_lis[i], consec_lis[i+1]) == (-1, 0)) ):
            num_valleys += 0.5
    """
        
    # 1 -1 -1 -1  1 -1  1 1
    # 1  0 -1 -2 -1 -2 -1 0
    return int(num_valleys)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
