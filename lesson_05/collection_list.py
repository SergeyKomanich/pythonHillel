# list

lst = []
print(lst, type(lst))

lst = [2, 6, 5.4, 'Hello', True]
print(lst, type(lst))

lst = list()
print(lst, type(lst))

lst = list('Hello World!')
print(lst, type(lst))

lst = list(str(123456))
print(lst, type(lst))

x = 123456
lst = list(str(x))
print(lst, type(lst))

x1 = [1, 2, 3, 4, 5]
x2 = [6, 7, 8, 9, 0]
x3 = x1 + x2
print(x3)

# list1.extend(list2)
print(x1, id(x1))
x1.extend(x2)
print(x1, id(x1))

x4 = x1 * 3
print(x4)

x5 = [0] * 10
print(x5)

lst = list('Process finished')
# len()
print(len(lst))

# in, not in
print('o' in lst)
print('a' not in lst)

lst = [4, 7, 2, 3, 7, 3, 9, 3, 1, 7, 3, 9, 4, 3, 8, 4]
# min, max, sum
print(min(lst))
print(max(lst))
print(sum(lst))

# list.index(x)
print(lst.index(8))
# print(lst.index(23))

# list.count(x)
print(lst.count(3))
print(lst.count(34))

# list.pop(), list.pop(idx)
print(lst)
print(lst.pop())
print(lst)
print(lst.pop(3))
print(lst)

# list.append(value)
lst.append(55)
print(lst)

# list.insert(idx, value)
lst.insert(3, 44)
print(lst)

# list.clear()
# lst.clear()
# print(lst)

# list.remove(value)
lst.remove(3)
print(lst)
# lst.remove(33)

for _ in range(lst.count(3)):
    lst.remove(3)
print(lst)

# del list[idx]
del lst[3]
print(lst)

# del lst
# print(lst)

# list.revers()
lst.reverse()
print(lst)

lst1 = lst[::-1]
print(lst1, id(lst), id(lst1))

# split(), join()
s = 'Process finished with exit code 0'
lst = s.split()
print(lst)

s1 = ' - '.join(lst)
print(s1)

'<br/>'
