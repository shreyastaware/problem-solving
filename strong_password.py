#!/bin/python3
# 03/05/2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-strong-password/problem

"""
Problem:

Given a password, find the minimum number of characters to add to make it strong.

Solution:

The answer is always `max(6-n, 4-d)` where `n` is string length and `d` is the number of different type of 
characters that are already present in the input password.

"""

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

# using regex Method #2
def minimumNumber1(n, password):
    MIN_LENGTH = 6
    charsToChange = 0
    
    if not re.search('[0-9]', password): charsToChange += 1
    if not re.search('[A-Z]', password): charsToChange += 1
    if not re.search('[a-z]', password): charsToChange += 1 
    if not re.search(r'[!@#$%^&*()\-+]', password): charsToChange += 1
    
    return max(MIN_LENGTH - len(password), charsToChange) if n < 6 else charsToChange

# Initial Method #1
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
        
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    pas = set(password)
    
    if n < 6:
        min_chars_req = 0
        nums = 0
        lo = 0
        hi = 0
        sp = 0
        for char in pas:
            if char in numbers:
                nums += 1
            elif char in lower_case:
                lo += 1
            elif char in upper_case:
                hi += 1
            elif char in special_characters:
                sp += 1
                
        if nums == 0:
            min_chars_req += 1
            
        if lo == 0:
            min_chars_req += 1
            
        if hi == 0:
            min_chars_req += 1
            
        if sp == 0:
            min_chars_req += 1
            
        if n + min_chars_req < 6:
            min_chars_req = 6 - n
            
    else:
        min_chars_req = 0
        nums = 0
        lo = 0
        hi = 0
        sp = 0
        for char in pas:
            if char in numbers:
                nums += 1
            elif char in lower_case:
                lo += 1
            elif char in upper_case:
                hi += 1
            elif char in special_characters:
                sp += 1
                
        if nums == 0:
            min_chars_req += 1
            
        if lo == 0:
            min_chars_req += 1
            
        if hi == 0:
            min_chars_req += 1
            
        if sp == 0:
            min_chars_req += 1
            
    return min_chars_req

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
