#!/bin/python3

"""
Pre-requisites: Sorting, Implementation Skills.

Difficulty Level: Easy.

Hints: Sort the input n numbers.

Editorial:

The naive solution for this problem is to use two loops. For every number (a[i]), loop over all the 
numbers to find the optimum number (b[i]) where abs(a[i]-b[i]) is minimum. Then, choose the minimum 
value among all the pairs. This solution has a time complexity O(N^2) which will cause the Time Limit 
Exceeded issue. Therefore, you need to think in another way to find the closest number.

Sort the input array in ascending order. The closest number (b[i]) to a number (a[i]) will be either the number 
before or after it in the list. Calculate the difference between every successive pair and minimize the 
output answer. In case there is more than one pair matching the minimum, use a vector to store all of 
the pairs.

Time Complexity: O(N*LOG(N))
Memory Space Complexity: O(N)
"""

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    pairs = []
    minDiff = 1000000000000001
    for i in range(1,len(arr)):
        d = abs(arr[i] - arr[i-1])
        if d < minDiff:
            pairs = [arr[i-1],arr[i]]
            minDiff = d
        elif d == minDiff:
            pairs.extend([arr[i-1],arr[i]])
            
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()