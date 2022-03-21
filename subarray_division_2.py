#!/bin/python3
# 21 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-the-birthday-bar/problem

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

# Note - for consecutive array question; create sum array and then iterate through sum array
#  for O(n) solution

def birthday_consecutive(s, d, m):

    sum_array = s.copy()
    n = len(sum_array)

    for i in range(1, n):
        sum_array[i] += sum_array[i-1]

    num_ways = 1 if (n >= m and sum_array[m-1] == d) else 0

    for i in range(1, n):

        if sum_array[i] - sum_array[i-m] == d:
            num_ways += 1

    return num_ways




def birthday(s, d, m):
    # Write your code here
    
    num_ways = 0
    
    for i in range(len(s)-m+1):
        
        if sum(s[i:i+m]) == d:
            num_ways += 1
            
    return num_ways
        
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
