from string import lowercase, lower
s = input().lower() # lowercase input
s = list(set(s)-set(' ')) # remove ' ' spaces
s = ''.join(sorted(s)) # joined the sorted list of unique charaters
print(["not pangram", "pangram"][lowercase == s])