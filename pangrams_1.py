from string import lowercase, lower
print(["not pangram", "pangram"][lowercase == ''.join(sorted(list(set(input().lower())-set(' '))))])