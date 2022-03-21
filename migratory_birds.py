#!/bin/python3
# 21 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-migratory-birds/problem

"""
Observation
As we go through the list of birds, we'll need to keep track the number of birds of each type. 
If we don't do this, then we can't determine which type of bird is the most common.

Possible Solution
To keep track of the frequency of each type, we can create an integer array of size 6 (comment A) and use 
index locations 1 through 5 to maintain a count of the number of birds for each ID type from 1 through 5
 (you can also use a 5-cell array, but this removes the need to offset the index by 1).

Next, we'll traverse through the array of birds (comment B) and increment the value at the array index 
corresponding to the ID type of that bird (comment C — note that the cells of integer arrays in Java are 
initialized to 0 by default).

Once we've determined the frequency of each type of bird, we iterate through our frequency array (comment D) 
and compare the values at each index (comment E). Each time a new value is strictly larger than the previous 
value, we update a variable that tracks the type having the maximum frequency. Because we're iterating 
through the list from smallest ID to largest, this ensures that we are always choosing the smallest ID 
number in instances where two or more types have the same frequency. After performing all five comparisons, 
we print the value of our variable tracking the ID type with the maximal frequency.

Notes
This approach requires that we perform an operation on each element of input and then perform 5 operations 
regardless of the input size, so the complexity of this approach is O(n). What other approaches might allow for 
shortcuts or faster determination?
"""

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    max_lis = []
    max_count = 0
    
    for ele in set(arr):
        max_count = max(max_count, arr.count(ele))
    
    for ele in set(arr):
        if arr.count(ele) == max_count:
            max_lis.append(ele)
            
    return min(max_lis)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
