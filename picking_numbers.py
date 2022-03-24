# 24 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-picking-numbers/problem

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

