
lis = list(range(11))
dig_len = 1

for i in range(0, len(lis), dig_len):

    if lis[i] % 2 == 0:
        dig_len += 1

    print(lis[i])

i = 0
dig_len = 1
while i < len(lis):

    print(lis[i])

    if lis[i] % 2 == 0:
        dig_len += 1
        i += dig_len
    else:
        i += 1
