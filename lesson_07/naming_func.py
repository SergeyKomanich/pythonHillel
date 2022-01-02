import random

"""
def function_name(param1, param2):
    operator 1
    operator 2

"""

lst = [random.randint(10, 50) for _ in range(15)]
lst1 = [random.randint(10, 50) for _ in range(15)]


def print_list(param):
    for i in range(len(param)):
        print(param[i], '<->', end=' ')
    print()


def sum_list(param):
    s = 0
    for i in range(len(param)):
        s += param[i]
    return s


def multi_func(my_list):
    s = 0
    p = 1
    for element in my_list:
        s += element
        p *= element
    return s, p


# for i in range(len(lst)):
#     print(lst[i], '<>', end=' ')
# print()
print_list(lst)

lst = [el+5 for el in lst]

# for i in range(len(lst)):
#     print(lst[i], '<>', end=' ')
# print()
print_list(lst)

lst = [el*2 for el in lst]

# for i in range(len(lst)):
#     print(lst[i], '<>', end=' ')
# print()
print_list(lst)
print_list(lst1)

x = sum_list(lst)
y = sum_list(lst1)
res = sum_list(lst) + sum_list(lst1)
print(x, y, x + y, res)

z = multi_func(lst)
print(z, z[0], z[1])
b, c = z
print(b, c)
a, b = multi_func(lst1)
print(a, b)
