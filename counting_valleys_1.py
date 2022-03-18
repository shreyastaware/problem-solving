"""
Our goal is to count the number of valleys. A valley is a sequence of steps starting with a step 
downward from sea level and ending with a step upward to sea level. Let `level` be a variable denoting the 
current altitude. If we take a step upwards,  is incremented by one; if we take step downwards, `level` is 
decremented by one.

Since we know that the sequence of input steps starts and ends at sea level, then we can say that our  
`level` variable is 0 at the beginning and end of the hike. The number of valleys can be counted as the 
number of steps taken upwards to sea level (i.e., when `level` goes from -1 to 0. This is true, because 
each such step ends the sequence of steps below sea level, signifying the end of a valley.
"""

# Solution uses a two pointer technique, 
# we check if current step leads to height 0 and previous height was -ve.  
height = 0
prev_height = 0
cnt = 0
n = input()
s = input().strip()
for i in range(len(s)):
    if (s[i] == 'U'):
        height += 1
    elif s[i] == 'D':
        height -= 1
    if height == 0 and prev_height < 0:
        cnt += 1
    prev_height = height
print(cnt)
