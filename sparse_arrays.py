# 15 03 2022 Tuesday
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-sparse-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings_official_answer(strings, queries):
    words = dict()
    ans = []
    for w in strings:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1
    for q in queries:
        if q in words:
            ans.append(words[q])
        else:
            ans.append(0)
    return ans

# O(n*q*20) worst time complexity
# O(n) worst case space complexity

def matchingStrings(strings, queries):
    # Write your code here
    freq = []
    for query in queries:
        freq.append(strings.count(query))
        
    return freq

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()


