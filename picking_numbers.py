# 24 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-picking-numbers/problem

"""
Observation:

The absolute difference between any two of the chosen integers must be <= 1, so we need to choose our 
integers in either of the following ways:

-> We choose all occurrences of one particular integer so that each pair of integers in the multiset has an 
absolute difference of 0. For example, if a = [1, 4, 4, 4, 4], we choose {4, 4, 4, 4}.

-> We choose all occurrences of two particular integers that differ by  so that each pair of integers 
in the multiset has an absolute difference of either 0 or 1. For example, if a = [1, 2, 2, 2, 4, 5], 
we choose {1, 2, 2, 2}.

Solution:

To solve this challenge, we perform the following steps:

Get the frequency of each number, `cnt1, cnt2,...,cnt99` (recall that 0 < ai < 100).
Find and print the maximal value of any cnt(i) + cnt(i+1) or cnt(i) if there is not an 
appropriate value to pair with.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    
    b = sorted(list(set(a)))
    
    # a.sort()
    lis_of_arrays = []
    
    unique_set = set()
    begin = 0
    end = 0
    max_sum = 0
    
    for i in range(len(b)):
        
        if b[i] not in unique_set:
            unique_set.add(b[i])
            
        if max(abs(b[i] - min(unique_set)), abs(b[i] - max(unique_set))) <= 1:
            end += 1
        else:
            max_sum = max( max_sum, sum( [a.count(ele) for ele in b[begin:end] ]  ) )
            # lis_of_arrays.append((b[begin:end]))
            begin = end
            end += 1
            unique_set.clear()
            unique_set.add(b[i])
    
    if max_sum == 0 and len(b) == 1:
        max_sum = len(a)
    elif max_sum <= 1:
        max_sum = 0
            
    return max_sum
    
    """
    # Method 2
    
    a.sort()
    lis_of_arrays = []
    
    unique_set = set()
    begin = 0
    end = 0
    
    for i in range(len(a)):
        
        if a[i] not in unique_set:
            unique_set.add(a[i])
            
        if max(abs(a[i] - min(unique_set)), abs(a[i] - max(unique_set))) <= 1:
            end += 1
        else:
            lis_of_arrays.append(len(a[begin:end]))
            begin = end
            end += 1
            unique_set.clear()
            unique_set.add(a[i])
    
            
    return max(lis_of_arrays)
    """
    
    
    """
    # Solved considering solid sub-array
    
    lis_of_arrays = []
    
    unique_set = set()
    begin = 0
    end = 0
    
    for i in range(len(a)):
        
        if a[i] not in unique_set:
            unique_set.add(a[i])
            
        if max(abs(a[i] - min(unique_set)), abs(a[i] - max(unique_set))) <= 1:
            end += 1
        else:
            lis_of_arrays.append(len(a[begin:end]))
            begin = end
            end += 1
            unique_set.clear()
            unique_set.add(a[i])
    
            
    return max(lis_of_arrays)
    """
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

