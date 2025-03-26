
import pdb;pdb.set_trace()

def squares(lst1):

    dict1 = {}

    for x in lst1:
        dict1[x] = x**2

    return dict1

lst1 = [1, 2, 3, 4]
dict1 = squares(lst1)

print('the squares of the numbers are - {}'.format(dict1))

"""
output: d:\pythonprogramms\squares_of_keys.py(3)<module>()
-> def squares(lst1):
(Pdb) n
> d:\pythonprogramms\squares_of_keys.py(12)<module>()
-> lst1 = [1, 2, 3, 4]
(Pdb) n
> d:\pythonprogramms\squares_of_keys.py(13)<module>()
-> dict1 = squares(lst1)
(Pdb) c
the squares of the numbers are - {1: 1, 2: 4, 3: 9, 4: 16}S
"""
