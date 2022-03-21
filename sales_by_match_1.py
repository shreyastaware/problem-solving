# To solve this challenge, we go through each color i and count its frequency, f(i). 
# Once we've calculated all the frequencies, we calculate the number of pairs of each 
# kind of sock as f(i)/2 (using integer division). Finally, we print the total sum of all pairs of socks.

from itertools import groupby
n = int(input())
c = map(int, input().split())

ans = 0
for val in [len(list(group)) for key, group in groupby(sorted(c))]:
    ans = ans + val/2
print(ans)
