#!/bin/python3
# 21 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-maximum-perimeter-triangle/problem

"""
Sort the list of lengths in decreasing order. Beginning with the first element, the longest stick, 
store the value to S. Check to see if the next two sides sum to greater than S. If so, that's your answer. 
If not, store the next element to S and repeat until you find a non-degenerate triangle or determine it is 
impossible.
"""


import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle_solution(sticks):
    """
    Simpler Solution as mentioned in lines 6 to 9
    """

    sticks.sort(reverse = True)

    for i in range(len(sticks)-2):
        
        # as we are checking triangle degeneracy for longer side, for other short side
        # it will of course be satisfied
        if sticks[i] >= sticks[i+1] + sticks[i+2]: 
            continue
        else:
            return sticks[i:i+3]


    pass

def degenerate(a, b, c):
    """
    Returns whether a triangle is degenerate or not
    """
    
    if a+b > c and b+c > a and a+c > b:
        return False
    else:
        return True
    

def maximumPerimeterTriangle(sticks):
    # Write your code here
    triplets = []
    
    for i in range(len(sticks)):
        for j in range(i+1, len(sticks)):
            for k in range(j+1, len(sticks)):
                if not degenerate(sticks[i], sticks[j], sticks[k]):
                    triplets.append((sticks[i], sticks[j], sticks[k]))
    # triplets = [(a, b, c) for a in sticks for b in sticks for c in sticks if a != b and b != c]
    max_sum = 0
    max_side = 0
    max_peri_triplets = []
    
    if len(triplets) == 0:
        return [-1]
    
    for a, b, c in triplets:
        max_sum = max(max_sum, a+b+c)
        
    for a, b, c in triplets:
        if max_sum == a+b+c:
            max_peri_triplets.append((a, b, c))
            
    max_side = 0
    for a, b, c in max_peri_triplets:
        max_side = max(max_side, a, b, c)
    
    max_peri_side_triplets = []
    for a, b, c in max_peri_triplets:
        if max_side == max(a, b, c):
            max_peri_side_triplets.append((a, b, c))
    
    longest_min_side = 0
    for a, b, c in max_peri_side_triplets:
        longest_min_side = max(longest_min_side, min(a, b, c))
        
    longest_min_side_max_peri_side_triplets = []
    for a, b, c in max_peri_side_triplets:
        if longest_min_side == min(a, b, c):
            longest_min_side_max_peri_side_triplets.append((a, b, c))
            
    return sorted(longest_min_side_max_peri_side_triplets[0])
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
