#!/bin/python3
# 07 04 2022
# Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-caesar-cipher-1/problem

"""
To encrypt the string, we need to rotate the alphabets in the string by a number k. If k is a multiple of 26, 
then rotating the alphabets in the string by k has no effect on the string. Rotation by k is same as rotation 
by k+26. So by taking modulo of k with 26, we get the number of times we need to rotate the alphabets of the 
string. To rotate the alphabets in a string by a value k, we add k to the character. If this value exceeds 
the range of the alpabets, we need to wrap it back. The range of uppercase characters is from 65 ('A') to 
90 ('Z'). The range of lowercase characters is from 97 ('a') to 122 ('z').
Example: For the string : "middle-Outz" and k=2
We add 2 to 'm'. 'm' becomes 'o'. This value is within the ascii range so we don't need to wrap it. '-' 
remains unaltered. 'z' on adding 2 becomes 124. This value lies outside the range of lowercase characters. 
We need to wrap this value. By taking the modulo of this value with 122, and adding this value to 96('a'-1) 
we get the rotated character.

For lowercase characters,

// Let char c = s[i] be a lowercase character in the string.
k = k % 26;
c += k;
if(c > 122) {
    c = 96 + (c % 122);
}

"""

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher_1(s, k):

    k %= 26
    temp = list(map(ord, s))

    for i in range(len(s)):

        if 65 <= temp[i] <= 90:
            temp[i] += k
            temp[i] = (64 + (temp[i]%90) ) if temp[i] > 90 else temp[i]
        
        elif 97 <= temp[i] <= 122:
            temp[i] += k
            temp[i] = (96 + (temp[i]%122) ) if temp[i] > 122 else temp[i]

    return ("".join(map(chr, temp)))

def caesarCipher(s, k):
    # Write your code here
    
    k%=26
    
    lis = list(map(ord, s))
    
    for i, num in enumerate(lis):
        
        if (num in range(ord('A'), ord('Z')+1)) or (num in range(ord('a'), ord('z')+1)):
            
            if num >= ord('a') and (num+k) <= ord('z'):
                
                print('first', chr(num))
                lis[i] += k
                
            elif num >= ord('A') and (num+k) <= ord('Z'):
                
                print('second', chr(num))
                lis[i] += k
                
            else:
                
                print('third', chr(num))
                lis[i] -= (26 - k)
    
    print(lis)
    
    return "".join(tuple(map(chr, lis)))
        
            
    
    # rot = [ chr(num+2) if num in range(ord('a'), ) for num in lis ]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
