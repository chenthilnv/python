# Lists
lst = [1, 2, 3, 4]
lst.append(5)
lst.extend([6, 7])
lst.remove(2)
print("List:", lst)
print("List slicing:", lst[1:4])

# Tuples
tup = (10, 20, 30)
print("Tuple:", tup)
print("Tuple indexing:", tup[1])

# Sets
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
s.discard(2)
print("Set:", s)
print("Set operations:", s.union({7, 8}), s.intersection({3, 4, 5}), s.difference({1, 6}))

# Dictionaries
d = {'a': 1, 'b': 2}
d['c'] = 3
d.update({'d': 4})
del d['a']
print("Dictionary:", d)
print("Dictionary keys:", list(d.keys()))
print("Dictionary values:", list(d.values()))
print("Dictionary items:", list(d.items()))

# Dictionary comprehension
squared = {x: x*x for x in range(5)}
print("Dictionary comprehension:", squared)
