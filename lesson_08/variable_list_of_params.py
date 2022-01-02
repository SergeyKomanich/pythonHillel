
print()
print(1, 2.4, 'Test', True)
print(1, 2, 3, 4, 5, 6, 7, 8)


def func1(*args):
    # print(args, type(args))
    for param in args:
        print(param, end=' ')
    print()


func1()
func1(1, 2.4, 'Test', True)
func1(1, 2, 3, 4, 5, 6, 7, 8)


def func2(**kwargs):
    print(kwargs, type(kwargs))


func2()
func2(a=1, t=2.4, s='Test', b=True)
func2(x1=1, x2=2, x3=3, x4=4, y1=5, y2=6, y3=7, y4=8)


def func3(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


func3(func2)
func3(1, 2.4, 'Test', True, a=1, t=2.4, s='Test', b=True)
func3(1, 2, 3, 4, 5, 6, 7, 8, x1=1, x2=2, x3=3, x4=4, y1=5, y2=6, y3=7, y4=8)
