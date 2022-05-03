#!/usr/bin/python
    
N = input()
K = input()
    
assert 1 <= N <= 10**5
assert 1 <= K <= N
    
lis = []
for i in range(N):
    lis.append(input())
    
lis.sort()
    
for i in lis:
    assert 0 <= i <= 10**9
    
answer = 100000000000000000000
    
for index in range(N-K+1):
    diff = lis[index+K-1] - lis[index]
    
    if diff < answer:
        answer = diff
    
print (answer)