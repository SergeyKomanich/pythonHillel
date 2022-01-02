import random
"""
    lambda a1, b2, c3: (a1 + c3) * b2
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst1 = []
for el in lst:
    lst1.append(el + 1)
print(lst1)

lst3 = []
for i in range(len(lst)):
    if i % 2:
        lst3.append(lst[i] + 1)
    else:
        lst3.append(lst[i] * 2)
print(lst3)

# map, filter, zip
lst2 = list(map(lambda x: x+1, lst))
print(lst2)

lst = [random.randint(10, 99) for _ in range(15)]
print(lst)

lst4 = []
for el in lst:
    if el % 2:
        lst4.append(el)
print(lst4)


def func(x):
    return x % 2


lst5 = list(filter(func, lst))
print(lst5)
lst6 = list(filter(lambda x: x % 2, lst))
print(lst6)

lst1 = [1, 2, 3, 4, 5, 6]
lst2 = ['a', 'b', 'c', 'd', 'e', 'f']

# d1 = {}
# for i in range(len(lst1)):
#     d1[lst1[i]] = lst2[i]
# print(d1)

d2 = dict(zip(lst1, lst2))
print(d2)
