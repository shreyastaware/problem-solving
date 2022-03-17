# 17 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-diagonal-difference/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    length_of_column = len(arr)
    diag_1_sum, diag_2_sum = 0, 0
    
    """
    for i, row in enumerate(arr):
        for j, value in enumerate(row):
            if i == j and i + j == length_of_column - 1:
                diag_1_sum += arr[i][j]
                diag_2_sum += arr[i][j]
                
            elif i == j:
                diag_1_sum += arr[i][j]
                
            elif i + j == length_of_column - 1:
                diag_2_sum += arr[i][j]
    """         
    
    for i in range(length_of_column):
        for j in range(length_of_column):
            if i == j and i + j == length_of_column - 1:
                diag_1_sum += arr[i][j]
                diag_2_sum += arr[i][j]
                
            elif i == j:
                diag_1_sum += arr[i][j]
                
            elif i + j == length_of_column - 1:
                diag_2_sum += arr[i][j]
    
    return abs(diag_1_sum-diag_2_sum)

# Not a great solution as it is O(n^2)
# O(n^2) Time Complexity
# O(1) Space Complexity

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
