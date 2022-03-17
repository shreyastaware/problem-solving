# 17 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-flipping-bits/problem

#  You have only to properly use the '~' bitwise NOT operator. 
# Special care should be taken in languages with no unsigned integers to avoid overflows.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    
    # this works because 
    # 1111 (no of bit) - 1010 (value of number)
    # this will yield bitwise NOT of the integer
    # ~n yields bitwise NOT but it also include signed integers that 
    # is negative numbers so the answer will be -ve
    
    return 2**32 -1 - n
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
