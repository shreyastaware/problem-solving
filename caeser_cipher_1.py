n = int(input())

s = list(input())

k = int(input()) % 26

temp = list(map(ord, s))

"""

65 + ((temp[i] - 65) + k) % 26

(temp[i] - 65) brings the range from 0 to 25 both inclusive.

so when we add k which also is between 0 to 26.

Now we just want to remove extra above 26. So if 25 + 5 = 30 => 

we should do 30%26 = 4 

so 'Z' becomes 'E'
so 90 becomes (65 + 4) = 69

"""

for i in range(len(s)):

    if 65 <= temp[i] <= 90:
        temp[i] = 65 + ((temp[i] - 65) + k) % 26
    
    elif 97 <= temp[i] <= 122:
        temp[i] = 97 + ((temp[i] - 97) + k) % 26

print("".join(map(chr, temp)))