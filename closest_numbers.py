#!/bin/python3
# 29 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-closest-numbers/problem

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    
    arr.sort()
    
    lis_of_tups = [(i, j) for i, j in zip(arr[:-1], arr[1:])]
    
    lis_diff = [ (j - i) for i, j in zip(arr[:-1], arr[1:]) ]
    
    min_diff = min(lis_diff)
    
    indices = [i for i, ele in enumerate(lis_diff) if ele ==  min_diff]
    
    lis = []
    for ind in indices:
        a, b = lis_of_tups[ind]
        
        lis.extend([a, b])
    
    return lis
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
