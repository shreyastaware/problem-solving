# 17 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-lonely-integer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

# Because we know all the elements are given in pairs except for the one we're looking for, the most efficient approach to this problem uses exclusive OR (XOR).
# Why does this work?
# When you XOR two bits together, matching values cancel each other out. For example, consider the following:
# XOR, 1 if the bits are different, 0 if they are the same.
# it means 1 XOR 1 = 0, 1 XOR 0 = 1, 0 XOR 1 = 1, 0 XOR 0 = 0
# So, if we XOR all the bits together, we get the unique bit.
# therefore, we can use XOR to find the unique bit.
# finally we can use the XOR to find the unique integer.

# Also, 0 XOR (any_number) = any_number

# 7 XOR 6 XOR 6 XOR 7 XOR 2
# 111 XOR 110 XOR 110 XOR 111 XOR 010
# 001 XOR 110 XOR 111 XOR 010
# 111 XOR 111 XOR 010
# 000 XOR 010
# 010
# Ans = 2


def lonelyinteger2(a):
    # Write your code here
    res=0
    for i in range(n):
        res=res^a[i] 
        # XOR Operation
    return res

def lonelyinteger(a):
    a_unique = set()
    ans = 0
    
    for ele in a:
        a_unique.add(ele)
    
    new_lis = list(a_unique)
    count_lis = [0]*len(new_lis)
    
    for ele in a:
        count_lis[new_lis.index(ele)] += 1
        
    for i, ind in enumerate(count_lis):
        if ind == 1:
            ans = new_lis[i]
            
    return ans

def lonelyinteger1(a):
    # Write your code here
    a_unique = set()
    ans = 0
    
    for ele in a:
        a_unique.add(ele)
    
    for ele in a_unique:
        if a.count(ele) == 1:
            ans = ele
        
    return ans
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

