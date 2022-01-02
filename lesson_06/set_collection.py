import random

s = {4, 6, 'Hello', True}
print(s, type(s))
s = {}
print(s, type(s))
s = set()
print(s, type(s))
s = set('Hello World!')
print(s, type(s))

for element in s:
    print(element, end=' ')
print()

# add
s.add(56)
print(s)
s.add(56)
print(s)

# remove, discard
s.remove('W')
print(s)
# s.remove('a')
# print(s)

s.discard('e')
print(s)
s.discard('A')
print(s)

x = s.pop()
print(x)
print(s)

# s1 = {random.randint(10, 20) for _ in range(15)}
# s2 = {random.randint(10, 20) for _ in range(15)}

s1 = {96, 34, 68, 87, 41, 76, 12, 92, 82, 21, 88, 61, 94, 95}
s2 = {39, 12, 41, 42, 11, 28, 47, 81, 21, 52, 85, 68, 87, 92}

print(s1)
print(s2)

# A | B        A.union(B)
# A |= B       A.update(B)
s3 = s1 | s2
print(s3)

# A & B        A.intersection(B)
# A &= B       A.intersection_update(B)
s3 = s1 & s2
print(s3)

# A - B        A.difference(B)
# A -= B       A.difference_update(B)
s3 = s1 - s2
print(s3)

# A ^ B        A.symmetric_difference(B)
# A ^= B       A.symmetric_difference_update(B)
s3 = s1 ^ s2
print(s3)

sx = s1 - s2
sy = s2 - s1
sz = sx | sy
print(sz)

print(s3 == sz)

sa = {1, 2, 3, 4}
sb = {1, 2, 2, 3, 4}
print(sa == sb)

fs = frozenset(s1)
print(fs, type(fs))

