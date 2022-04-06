#!/bin/python3
# 06 04 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-minimum-absolute-difference-in-an-array/problem

"""
Observation
The most obvious approach is find the minimum absolute difference between each number in the array and 
each other number in the array, and then take the minimum of those results. That approach is not ideal 
because we would need to find the difference between the first element and the (n-1) elements to its right, 
the second element and the (n-2) elements to its right, the third element and the (n-3) elements to its 
right, and so on.

Instead, we can simply sort the array to ensure that the absolute difference between each element and its 
adjacent element(s) is minimal. Working with sorted data allows us to minimize the number of calculations 
by simply finding the difference between each pair of adjacent elements in the sorted array. For example, 
if A = [10, 1, 5, 9], it becomes A = [1, 5, 9, 10] once sorted; we then simply find the minimum 
difference between (1, 5), (5, 9), and (9, 10).

Solution:

1. Sort the array of `n` numbers using a built-in method in your submission language of choice (you can write a 
sorting algorithm yourself, but built-in methods are almost always faster).

2. Create a variable to track the running minimum absolute difference between any two elements and initialize 
it to some valid possible minimum (e.g., the absolute difference between the highest and lowest possible 
values for `a(i)` in the Constraints, the absolute difference between the first and last elements of the sorted 
array, etc.).

3. Iterate through the array and calculate the absolute value of the difference between each pair of adjacent 
elements. You can alleviate the need to take the absolute value of the difference between `a(i)` and `a(i+1)` by 
calculating the difference as `a(i+1) - a(i)`; this is because sorting ensures that `a(i)` is always <= `a(i+1)` , 
so the result of this calculation will always be positive.

4. Check the absolute difference between each adjacent pair of elements against the running minimum absolute 
difference variable. If the absolute difference between some pair of adjacent elements is less than the value 
stored in the running minimum variable, set that pair's absolute difference as the new running minimum.

5. Print the final value of the running minimum absolute difference variable.

"""

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

def minAbsDifference(arr):
    # Editorial Solution
    arr.sort()
    for i in range(n - 1):
        mini = min(mini, abs(arr[i] - arr[i+1]))
    return mini

def minimumAbsoluteDifference(arr):
    # Write your code here
    """
    Method 1
    
    Time Complexity: O(N**2)
    Space Complexity: O(N**2)
    
    tups = [(a, b) for i, a in enumerate(arr) for j, b in enumerate(arr) if i != j]
    minAbsDiff =  min([abs(a-b) for a, b in tups])
    """
    
    """
    Method 2
    
    Time Complexity: O(N**2)
    Space Complexity: O(N**2)
    
    tups = [(a, b) for a in arr for b in arr if a != b]
    
    minAbsDiff =  min([abs(a-b) for a, b in tups])
    """
    
    """
    Method 3
    
    Time Complexity: O(N**2)
    Space Complexity: O(N**2)
    
    if len(set(arr)) == len(arr):
        minAbsDiff = min([abs(a - b) for i, a in enumerate(arr) for j, b in enumerate(arr) if i != j])
    else:
        minAbsDiff = 0
    """
    
    """
    Method 4
    
    Time Complexity: O(N)
    Space Complexity: O(N)
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
