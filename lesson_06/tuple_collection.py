t = ()
print(t, type(t))
t = (5, 6, 7.8, 'Hello', True)
print(t, type(t))
t = tuple()
print(t, type(t))
t = tuple('Hello World!')
print(t, type(t))

print(t[0])
print(t[-1])

print(t[-23534634525354234: 6987659875976487647864: 2])

# t[5] = 'R'
# len()
print(len(t))

# +
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

t4 = t1 * 4
print(t4)

# in         not in
print(4 in t1)
print(2 in t1)
print(4 not in t1)

# for
for element in t1:
    print(element, end=' ')
print()

for i in range(len(t1)):
    print(t1[i], end=' ')
print()

# index(value, start, stop)
print(t1.index(2))

# count(value)
print(t1.count(3))
print(t1.count(9))

# min, max, sum

# const int a = 7.8
# final int a = 9

const = (9.8, 3.14)
const = 7

a = [1, 2, 3]
b = 1, 2, 3
print(b, type(b))

print(1, 4.5, 'Hello World!', True)

t = (50,)
print(t, type(t))


