#!/bin/python3
# 21 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-sock-merchant/problem

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    
    unique_socks = set(ar)
    num_pairs = 0
    
    for sock in unique_socks:
        
        num_pairs += ar.count(sock) // 2
        
    return num_pairs
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
