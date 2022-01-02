import pprint

"""
{
    key1: value1,
    key2: value2,
    key3: value3,
    key4: value4,
}
"""

d = {}
print(d, type(d))
d = {
    1: 'one',
    0: 'zero',
}
pprint.pprint(d)
print(d, type(d))
d = dict()
print(d, type(d))

d = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Marines'
}

print(d, type(d))
pprint.pprint(d)

d = dict(
    [
        ('Colorado', 'Rockies'),
        ('Boston', 'Red Sox'),
        ('Minnesota', 'Twins'),
        ('Milwaukee', 'Brewers'),
        ('Seattle', 'Marines')
    ]
)
pprint.pprint(d)

d = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Marines'
)
pprint.pprint(d)
print(d)

print(d['Boston'])

d['Texas'] = 'Red Bull'
pprint.pprint(d)
d['Boston'] = 'Red Sox Ex'
pprint.pprint(d)
d['Boston'] = ['Red Sox', 'Red Sox Ex']
pprint.pprint(d)

# key ==> str, int, tuple, frozenset
d[(1, 2)] = 'tuple'
pprint.pprint(d)
# d[['a', 'b']] = 'litters'
# pprint.pprint(d)
d[0] = 'zero'
pprint.pprint(d)

d = {
    0: 'zero',
    1: 'one',
    2: 'two',
}

print(d[0])
print(d[2])

person = {}
person['name'] = 'Ivan'
person['age'] = 34
person['children'] = ['Olga', 'Petr', 'Elena']
person['pets'] = {'cat': 'Fox', 'dog': 'Fido'}
pprint.pprint(person)

print(person['name'])
print(person['children'][1])
print(person['pets']['dog'])

teams = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Marines'
)

pprint.pprint(teams)
# value in dict       value not in dict
print('Boston' in teams)
print('Boston1' not in teams)

# len(obj)
print(len(teams))

# dict.clear()
# teams.clear()
# print(teams)

# dict[key]
# dict.get(key, default_value)
print(teams.get('Boston1', 'No team in dict'))

# dict.keys()
# dict.values()
# dict.items()
print(list(teams.keys()))
print(list(teams.values()))
print(list(teams.items()))

for key, value in teams.items():
    print(key, '-->', value)

t = 1, 2, 3, 4
a, b, c, d = (1, 2, 3, 4)

# dict.pop(key)
pprint.pprint(teams)
print(teams.pop('Boston'))
pprint.pprint(teams)

# dict.popitem()
pprint.pprint(teams)
print(teams.popitem())
pprint.pprint(teams)

# dict1.update(dict2)
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 300}

print(d1)
print(d2)
d1.update(d2)
print(d1)
print(d2)
