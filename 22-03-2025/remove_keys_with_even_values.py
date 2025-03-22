import pdb;pdb.set_trace()

def remove_even_keys(numbers):

    dict1 = {}
    for keys,values in numbers.items():

        if values % 2 != 0:
            dict1[keys] = values

    return dict1 

numbers = {'a': 4, 'b': 7, 'c': 10, 'd': 15}
dict1 =  remove_even_keys(numbers)

print('the values without even are - {}'.format(dict1))

''' 
output :
> d:\pythonprogramms\remove_keys_with_even_values.py(3)<module>()
-> def remove_even_keys(numbers):
(Pdb) n
> d:\pythonprogramms\remove_keys_with_even_values.py(13)<module>()
-> numbers = {'a': 4, 'b': 7, 'c': 10, 'd': 15}
(Pdb) dict1
*** NameError: name 'dict1' is not defined
(Pdb) n
> d:\pythonprogramms\remove_keys_with_even_values.py(14)<module>()
-> dict1 =  remove_even_keys(numbers)
(Pdb) c
the values without even are - {'b': 7, 'd': 15}

'''
