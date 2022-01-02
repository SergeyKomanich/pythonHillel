import random

# randint()
# randrange()
# random()
# uniform

# randrange(start, stop, step)

# range(1, 20, 2)       1, 3, 5, 7, 9, 11, 13, 15, 17, 19
# randrange(1, 20, 2)   5, 1, 15, 11, 9, 3, 7, 5, 3, 3, 7
for _ in range(15):
    print(random.randrange(1, 10), end=' ')
print()

# randint(start, stop)
for _ in range(15):
    print(random.randint(1, 10), end=' ')
print()

# random()      0 - 1
for _ in range(15):
    print(round(random.random(), 2), end=' ')
print()

# uniform(start, stop)
for _ in range(15):
    print(round(random.uniform(0.1, 20.9), 1), end=' ')
print()


