#!/bin/python3
# 29 03 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-separate-the-numbers/problem

"""
Observation

The challenge description says that the input string `s` cannot be beautiful if it only contains a 
single character. We can add an if statement in our code to ensure that NO is printed in this case. We 
also know that the input string can contain 32 characters maximum.

Solution
Our approach is to use brute force. We'll begin with the first, smallest number that can be made from 
the input string. We'll see if the next number that can be made from the input string is one greater than 
it, and if it is we'll create the next number in the sequence and again compare it. If at any moment our 
sequence fails to meet the conditions necessary we'll start back over at the beginning of the input 
string and create a new beginning to the sequence using a larger first number.

For example, given an input string `100101`, we'll begin by creating a sequence with `1` and we'll compare 
it with the next number for our sequence, `0`. This comparison will tell us that `0` is not one more 
than `1`, and since our first number (1) does not end with a `9` we'll not consider comparing it with 
another possible number that may have one more character. (Consider an input string `91011`. We'd want to 
compare `9` with `10` so we'll need to look out for 9's during our comparisons.) This sequence (beginning 
with 1 and then 0) will fail and we'll restart with `10` as our first number in the next potentially 
successfull sequence. We'll compare `10` to `01` (we'll choose two characters to create our number because 
we know that we can't use fewer characters than our first number because it would automatically be smaller) 
and this comparison will yet again lead to a failing sequence. We'll begin again with a new sequence 
beginning with `100` and will compare `100` to `101` and we'll find that the comparison meets our 
conditions and we'll continue through the input string to complete our sequence. Luckily our string is 
short so we're already done! We'll print YES 100 as our output (on its own line) and will move to the 
next query.

"""

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    
    glob_digit_len = 1

    while glob_digit_len < len(s):
        
        lis = []
        digit_len = glob_digit_len
        i = 0

        while i + digit_len <= len(s):
            
            # print(i)
            set_of_9s = set(s[i:i+digit_len])

            if  len(set_of_9s) == 1 and next(iter(set_of_9s)) == '9':

                j = i

                if s[j] == '9':
                    # figuring out size of digit_len if it is not 1
                    while s[j] == '9': 
                        j += 1
                        if j >= len(s):
                            break
                else:
                    break

                lis.append(s[i:j])
                
                digit_len = j - i + 1

                i = j

            else:
                lis.append(s[i:i+digit_len])
                i += digit_len
        
        if i < len(s) and i + digit_len > len(s):
            lis.append(s[i:i+digit_len])

        t = [int(ele) for ele in lis]

        if len(t) >= 2:
            # print(t)
            # print(t[:-1])
            # print(t[1:])
            set_of_1s = set([j-i for i, j in zip(t[:-1], t[1:])])
            # print(set_of_1s)
            if len(set_of_1s) == next(iter(set_of_1s)) == 1:
                # print('GLOBAL_DIGIT_LEN: ', glob_digit_len)
                if ( ( glob_digit_len == 1 and 
                        not any([ele[0] == '0' for ele in lis[1:]]) ) 
                        or 
                        ( glob_digit_len > 1 
                        and not any([ele[0] == '0' for ele in lis]) ) ):
                    print('YES', t[0])
                    break
        
        glob_digit_len += 1

        # print(lis)

    if glob_digit_len == len(s):
        print('NO')
    
    """
    digit_length = 1
    i = 0
    
    lis 
    
    while digit_length != len(s):
        
        if (int(s[i:i+digit_length]) + 1) % 10 == 0:
            break
        
        if int(s[i:i+digit_length]) - int(s[i+digit_length:i+2*digit_length]) == -1:
            break
        else:
            digit_length += 1
    """
            
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

