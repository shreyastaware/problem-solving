#!/bin/python3
# 30 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-tower-breakers-1/problem

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#



def bestMove(lis, factors, player_num = 1):
    pass

def who_wins(lis, factors, player_num = 1):
    
    if len(lis) == 1:
        m = next(iter(set(lis)))
        return 1
    else:
        
        
        
    
    pass 
    
def towerBreakers(n, m):
    # Write your code here
    
    factors = set()
    
    for i in range(1, m):
        if m%i == 0: 
            factors.add(i)
            
    factors = sorted(list(factors))
    
    print(factors)
    
    player_num = who_wins([m]*n, factors)
    
    return player_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
