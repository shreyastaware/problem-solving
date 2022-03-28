#!/bin/python3
# 28 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-kangaroo/problem

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    
    # edge case
    if v1 == v2 and x1 != x2:
        return 'NO'
    
    elif ( (x2-x1) % (v1-v2) == 0 # ensuring jumps is an integer
                and 
            (x2-x1) / (v2-v1) < 0 # so that overtaking is possible
    ):
        return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
