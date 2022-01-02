import math


def square(side_size):
    P = side_size * 4
    S = side_size ** 2
    # D = round(math.sqrt(side_size ** 2 * 2), 2)
    D = math.sqrt(side_size ** 2 * 2)

    return P, S, D


res = square(5)
print(res, type(res))
print(square(5))
p, s, d = square(5)
# d = round(d, 2)
print(p, s, round(d, 2))
