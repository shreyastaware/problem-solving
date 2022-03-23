# Between two sets
# 23 03 2022
# Link: https://www.hackerrank.com/test/3g7so2i3ha1/questions/38ja2jois2r

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# Time Complexity = O( max ( len(a) * len(a), len(unique_multiples) * len(b) ) )
# Space Complexity = O( len(unique_multiples) )

def getTotalX(a, b):
    # Write your code here
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    
    unique_multiples = set()
    
    for ele_i in a:
        cnt = 0
        for ele_j in a:
            if ele_i < ele_j:
                continue
            else:
                if ele_i % ele_j == 0:
                    cnt += 1
        if cnt == len(a):
            unique_multiples.add(ele_i)
    
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i]*a[j] > b[0]:
                break
            else:
                unique_multiples.add(a[i]*a[j])
                
    
    copy_set = unique_multiples.copy()
    for ele in copy_set:
        inc = 1
        while(ele*inc <= min(b)):
            unique_multiples.add(ele*inc)
            inc += 1
    
    between_integers = 0
    
    for num_u in unique_multiples:
        
        count = 0
        for num_b in b:
            
            if num_b % num_u == 0:
                count += 1
                
        if count == len(b):
            between_integers += 1
            
    return between_integers
            
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

