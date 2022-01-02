from pprint import pprint
lst = {c: chr(c) for c in range(32, 128)}
# pprint(lst)

lst1 = [c for c in range(32, 128)]
lst2 = [chr(c) for c in range(32, 128)]
res1 = dict(zip(lst1, lst2))
res2 = dict(zip(lst2, lst1))
pprint(res2)
