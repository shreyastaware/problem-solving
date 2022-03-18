#  You have only to properly use the '~' bitwise NOT operator. 
# Special care should be taken in languages with no unsigned integers to avoid overflows.

#Another solution
for _ in range(int(input())):
    s = 2**32 ^ int(input())
    t = str(bin(s))[2:]
    t = t.replace('0','2')
    t = t.replace('1','0')
    t = t.replace('2','1')
    print(int(t,2))
