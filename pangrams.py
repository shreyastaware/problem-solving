#!/bin/python3

# 19 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-pangrams/problem

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    word_list = [word.lower() for word in s.split(' ')]
    unique_letters = set("".join(word_list))
    
    if len(unique_letters) == 26:
        return 'pangram'
    else:
        return 'not pangram'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
