
#Create a dictionary from two lists
import pdb;pdb.set_trace()

def list_to_dict(keys, values):
    dict1 = dict(zip(keys, values))

    return dict1

keys = ['a', 'b', 'c']
values =  [1, 2, 3]

print(list_to_dict(keys, values))


def list_to_dicts(keys, values):

    dict1 = {}

    for x in range(len(keys)):
        dict1[keys[x]] = values[x]

    return dict1

keys = ['a', 'b', 'c']
values = [1, 2, 3]

dict1 = list_to_dicts(keys, values)

print('the key, values are :{}'.format(dict1))

#output:
> d:\pythonprogramms\lists_to_dict.py(4)<module>()
-> def list_to_dict(keys, values):
(Pdb) n
> d:\pythonprogramms\lists_to_dict.py(9)<module>()
-> keys = ['a', 'b', 'c']
(Pdb) n
> d:\pythonprogramms\lists_to_dict.py(10)<module>()
-> values =  [1, 2, 3]
(Pdb) print(dict1)
*** NameError: name 'dict1' is not defined
(Pdb) n
> d:\pythonprogramms\lists_to_dict.py(12)<module>()
-> print(list_to_dict(keys, values))
(Pdb) n
{'a': 1, 'b': 2, 'c': 3}
> d:\pythonprogramms\lists_to_dict.py(15)<module>()
-> def list_to_dicts(keys, values):
(Pdb) n
> d:\pythonprogramms\lists_to_dict.py(24)<module>()
-> keys = ['a', 'b', 'c']
(Pdb) n
> d:\pythonprogramms\lists_to_dict.py(25)<module>()
-> values = [1, 2, 3]
(Pdb) n
> d:\pythonprogramms\lists_to_dict.py(27)<module>()
-> dict1 = list_to_dicts(keys, values)
(Pdb) n
> d:\pythonprogramms\lists_to_dict.py(29)<module>()
-> print('the key, values are :{}'.format(dict1))
(Pdb) print(dict1)
{'a': 1, 'b': 2, 'c': 3}
(Pdb)
{'a': 1, 'b': 2, 'c': 3}
(Pdb) c
the key, values are :{'a': 1, 'b': 2, 'c': 3}
PS D:\pythonprogramms>
