#!/bin/python3
# 22 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-drawing-book/problem

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here'
    
    if p%2 == 0:
        return min( p // 2, ((n-p) // 2))
    else:
        ele = (n-p)//2 if n%2 != 0 else ((n-p) // 2)+1
        return min( (p-1) // 2,  ele)
    
    """
    lis = [1]
    
    for i in range(2, n, 2):
        lis.append((i, i+1))
    
    if lis[-1][-1] != n:
        lis.append(n)
    
    # print(lis)
    lcount = 0
    rcount = len(lis)-1
    for i, tup in enumerate(lis):
        
        # print(i, tup)
        if i == 0 or (i == len(lis)-1 and n%2 == 0):
            
            # print(i, tup, 'first')
            if p == tup:
                return 0
            
        elif i == len(lis) - 1 and n%2 != 0:
            
            # print(i, tup, 'second')
            if p in tup:
                return 0
            
        else:
            lcount += 1
            rcount -= 1
            
            # print(i, tup, 'third')
            if p <= tup[1]:
                break
            
    return min(lcount, rcount)
    """
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
