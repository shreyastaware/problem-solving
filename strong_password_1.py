from string import digits, ascii_lowercase, ascii_uppercase
input()
s = input()

print(max(6 - len(s), sum(not (set(st) & set(s)) for st in (digits, ascii_lowercase, ascii_uppercase, "!@#$%^&*()-+"))))