import random

lst = []
for _ in range(25):
    lst.append(random.randint(10, 99))

print(lst)

for i in range(len(lst)):
    print(lst[i], end=' ')
    # lst[i] = 0
print()

for value in lst:
    print(value, end=' ')
print()

# variable = [expression1 expression2 expression3]
# 2 - 1
# 2 - 3 -1

lst = [random.randint(10, 99) for _ in range(15)]
print(lst)

lst1 = [value for value in lst if value % 2 != 0]
print(lst1)

s = ' + '.join([str(value) for value in lst]) + ' = ' + str(sum(lst))
print(s)
