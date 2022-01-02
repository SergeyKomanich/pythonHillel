"""
for variable in iterable_object:
    operator1
    operator2


for _ in iterable_object:
    operator1
    operator2
"""

# range(start, stop, step)
# range(start, stop)
# range(stop)

# 1     10      2
# 1 3 5 7 9

for i in range(16):
    print(i, end=' ')
print()

for i in range(1, 16):
    print(i, end=' ')
print()

s = 'Hello World!'
for el in s:
    print(el, end=' ')
print()

for _ in range(10):
    print('*', end='')
print()
