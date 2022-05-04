# 04/05/2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-smart-number/problem

"""
Because factors are in pairs. Let's take 12 for example, it has the following pairs of factors:

1 * 12
2 * 6
3 * 4
Since factors are always in pairs, the total number of factors must be even, unless there is a pair 
with two identical factors, like 9 = 3 * 3.

So, a smart number is a number which has a pair of factors with two identical numbers.

or a smart number is a perfect square.
"""

import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / val == val:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")

