import random
import pprint
import copy

# lst = [random.randint(10, 99) for _ in range(15)]
lst = [37, 92, 32, 42, 16, 87, 23, 72, 48, 46, 48, 46, 66, 11, 69]

print(lst)

a = 8
b = a

lst1 = lst
print(id(lst), id(lst1))
print(lst)
print(lst1)
lst[4] = 888
print(lst, id(lst))
print(lst1, id(lst1))

lst2 = []
for i in range(len(lst)):
    lst2.append(lst[i])

print(lst2, id(lst2))
lst[8] = 999
print(lst, id(lst))
print(lst2, id(lst2))

lst3 = lst[:]
print(lst, id(lst))
print(lst3, id(lst3))

lst4 = lst.copy()
print(lst4, id(lst4))

matrix = []
for _ in range(5):
    matrix.append([random.randint(10, 99) for _ in range(6)])
print(matrix)

pprint.pprint(matrix)

print(matrix[0][4])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

lst6 =[[26, 97, 21, 30, 29, 13],
[34, 47, 27, 80, 71, 71],
[73, 73, 91, 78, 97, 31],
[98, 38, 19, 54, 93, 19],
[93, 76, 46, 20, 35, 16]]

print(id(lst6))
pprint.pprint(lst6)
lst7 = lst6.copy()
print(id(lst7))
pprint.pprint(lst7)
lst6[3][5] = 555
pprint.pprint(lst7)

lst8 = copy.deepcopy(lst6)
pprint.pprint(lst8)
lst6[2][3] = 111
pprint.pprint(lst6)
pprint.pprint(lst8)
