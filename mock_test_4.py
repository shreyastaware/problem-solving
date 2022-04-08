# Anagram
# 08 04 2022
# Link: 



#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from collections import Counter

def anagram(s):
    # Write your code here
    
    if len(s) < 1 or len(s) % 2 == 1:
        return -1
    
    a = sorted(list(s[:len(s)//2]))
    b = sorted(list(s[len(s)//2:]))
    
    c1 = Counter(a)
    c2 = Counter(b)
    
    diff_c = c1 - c2
    
    return sum(diff_c.values())
    """
    count = 0
    for i, j in zip(a, b):
        if i != j:
            count += 1
            
    return count
    """
    """
    a = set(s[:len(s)//2])
    b = set(s[len(s)//2:])
    
    new_elements_required = a - b
    
    return len(new_elements_required)
    """
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
