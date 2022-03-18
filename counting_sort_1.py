# 18 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-countingsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    freq_arr = [0]*(max(arr) + 1)
    
    for i in range(len(arr)):
        freq_arr[arr[i]] += 1
        
    if len(freq_arr) < 100:
        freq_arr.extend([0]*(100-len(freq_arr)))
        
    return freq_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
