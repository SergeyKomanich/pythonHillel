"""
if condition:
    operator1
    operator2

operator3
"""

a = 16
if a > 10:
    print('A more than 10')

print('End')

"""
if condition:
    operator1
    operator2
else:
    operator3
    operator4

operator5
"""

a = 6
if a > 10:
    print('A more than 10')
else:
    print('A less than 10')

print('End')


a = 1000
# if 0 < a <= 1000:
#     print('1%')
# else:
#     if 1000 < a <= 2000:
#         print('2%')
#     else:
#         if 2000 < a <= 5000:
#             print('3%')
#         else:
#             if 5000 < a <= 10000:
#                 print('5%')
#             else:
#                 print('10%')

if 0 < a <= 1000:
    print('1%')
elif 1000 < a <= 2000:
    print('2%')
elif 2000 < a <= 5000:
    print('3%')
elif 5000 < a <= 10000:
    print('5%')
else:
    print('10%')
