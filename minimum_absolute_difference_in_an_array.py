#!/bin/python3
# 06 04 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-minimum-absolute-difference-in-an-array/problem

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    """
    tups = [(a, b) for i, a in enumerate(arr) for j, b in enumerate(arr) if i != j]
    
    # tups = [(a, b) for a in arr for b in arr if a != b]
    
    minAbsDiff =  min([abs(a-b) for a, b in tups])
    """
    
    arr.sort()
    minAbsDiff = min([abs(b-a) for a, b in zip(arr[:-1], arr[1:])])
    
    return minAbsDiff
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
