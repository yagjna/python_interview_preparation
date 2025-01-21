
# to find keys in dictionary
dict1 = {"a":1, 'b':2, 'c':3}
print(dict1.keys())


#to find values in dictionary
print(dict1.values())

#to get keys,values
print('{}'.format(dict1.items()))

#to get a element
print('{}'.format(dict1.get('a', 1)))
print('{}'.format(dict1.get('z', 8)))

#to remove a key value pair in the dictionary and return that item
print('{}'.format(dict1.popitem()))

#to add a key value pair
print('{}'.format(dict1.setdefault('s', 7)))
print(dict1)

#output:
dict_keys(['a', 'b', 'c'])
dict_values([1, 2, 3])
dict_items([('a', 1), ('b', 2), ('c', 3)])
1
8
('c', 3)
7
{'a': 1, 'b': 2, 's': 7}
