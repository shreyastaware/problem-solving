#!/bin/python3
# 03/05/2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-angry-children/problem

"""
In this problem, we are given a list of `N` numbers, out of which `K` numbers are to be chosen such that the 
difference between max and min of `K` numbers is minimized.

Where unfairness co-efficient, D = max of chosen K numbers - min of chosen K numbers.

First, we claim that k such numbers can only be obtained if we sort the list and chose k contiguous 
numbers. This can easily be proven. Suppose we choose numbers X1, X2, X3,....Xr, Xr+1,....,XK (all are 
in increasing order but not contiguous in the sorted list) i.e. there exists a number p which lies 
between Xr and Xr+1. If we include this number and exclude X1, the new value of D will become |XK-X2| 
whereas the old value was |XK-X1|. As we know X1<=X2<=XK, the value of D decreases or remains same. 
Hence, if the chosen K points are not consecutive in the sorted list then we can apply these insertions 
one or more times to reduce the value of K.

So, the problem reduces to choosing K consecutive numbers in a sorted list for which the value of D 
is minimum. Which can be easily done by sorting the given number in O(NlogN) and calculating D for 
each group of K consecutive number in O(N-K) time.

Time Complexity: O(NlogN)
Space Complexity: O(K)
"""

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    
    arr.sort()

    mins = [(arr[i+k-1]-arr[i]) for i in range(len(arr)-k+1)]
    
    return min(mins)
    
    """
    global_minimum = arr[-1]
    
    for i in range(len(arr)-k+1):
        
        lis = arr[i:i+k]
        global_minimum = min(max(lis)-min(lis), global_minimum)
    
    return global_minimum
    """
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
