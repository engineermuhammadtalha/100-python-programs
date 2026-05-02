# merge dicts
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d={**d1, **d2}
print(d)  # Output: {'a': 1, 'b': 3, 'c': 4}  # 'b' from d2 overwrites 'b' from d1