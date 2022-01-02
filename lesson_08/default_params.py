def func1(param1, param2, param3, param4):
    pass


func1(1, 2, 3, 4)


def func2(param1, param2, param3=0, param4='Hello'):
    print(param1, param2, param3, param4)
    param4.replace(' ', '')


func2(1, 2, 3, '4')
func2(1, 2, 3)
func2(1, 2)

func2(param4='R', param2=3, param1='test')












# a = 8
# b = 34 if a > 10 else 'Hello'
# print(b)
#
# if a > 10:
#     b = True
