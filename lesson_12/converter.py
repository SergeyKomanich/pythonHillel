"""
0   '0'
1   '1'
2   '2'
.
.
.
9   '9'
10  'A'
11  'B'
12  'C'
"""


def converter(num, base):
    from string import ascii_uppercase
    line = '0123456789' + ascii_uppercase
    # tmp = []
    s = ''
    while num > 0:
        # tmp.append(line[num % base])
        # tmp.insert(0, line[num % base])
        s = line[num % base] + s
        num //= base        # num = num // base

    # tmp.reverse()
    # tmp = tmp[::-1]
    # return ''.join(tmp)
    return s


print(converter(123456, 16))        # 1E240
print(converter(123456, 2))         # 11110001001000000
print(converter(123456, 8))         # 361100
print(converter(123456, 10))
print(converter(123456, 25))
