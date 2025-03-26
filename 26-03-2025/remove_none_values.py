
import pdb;pdb.set_trace()

def remove_none_values(dict1):

    dict2 = {}

    for key, values in dict1.items():
        if type(values) == int:
            dict2[key] = values
    return dict2

dict1 = {'a': 1, 'b': None, 'c': 2, 'd': None}
dict2 = remove_none_values(dict1)

print('the values without none - {}'.format(dict2))

"""
output:> d:\pythonprogramms\remove_none_values.py(3)<module>()
-> def remove_none_values(dict1):
(Pdb) n
> d:\pythonprogramms\remove_none_values.py(12)<module>()
-> dict1 = {'a': 1, 'b': None, 'c': 2, 'd': None}
(Pdb) n
> d:\pythonprogramms\remove_none_values.py(13)<module>()
-> dict2 = remove_none_values(dict1)
(Pdb) n
> d:\pythonprogramms\remove_none_values.py(15)<module>()
-> print('the values without none - {}'.format(dict2))
(Pdb) c
the values without none - {'a': 1, 'c': 2}
"""
