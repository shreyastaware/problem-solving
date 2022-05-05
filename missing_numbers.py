#!/bin/python3
# 05/05/2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-missing-numbers/problem

"""
In the problem you are asked to print numbers that are present in `B` but not in `A`. And also the numbers 
should be distinct, i.e. if any particular number is missing two times you have to print it only once.

Take two arrays, one for `A` and one for `B`. `A[i]` denotes the frequency of `i` in `A`. 
Similarly, `B[i]` denotes the frequency of `i` in `B`.

Now if the frequency of any number in `B` is greater than the frequency of that number in `A` print the number.
"""

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers1(arr, brr):
    # for frequency/count sort, only need 101 elements
    # due to last constraint
    freq = [0]*101
    # bmin to adjust values
    bmin = min(brr)
    # count sort the arrays
    # increment frequency for original
    for v in brr:
        freq[v-bmin] += 1
    # decrement frequency for final
    for v in arr:
        freq[v-bmin] -= 1
    # and put together the answer, automatically sorted
    # if there is a value in freq, it means there were more in brr than arr
    ans = []
    for i in range(101):
        if freq[i]>0:
            ans.append(i+bmin)
    return ans

def missingNumbers(arr, brr):
    # Write your code here
    a = Counter(arr)
    b = Counter(brr)
    
    c = (b-a).keys()
    
    lis = list(c)
    
    lis.sort()
    
    return lis

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
