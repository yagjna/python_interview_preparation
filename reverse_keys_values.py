import pdb; pdb.set_trace()

def reverse_keys_values(dict1):
    dict2 = {} 
    for keys, values in dict1.items():  
        dict2[values] = keys

    return dict2

dict1 = {'a': 3, 'b': 1, 'c': 2}
dict2 = reverse_keys_values(dict1)

print('{}'.format(dict2))  

'''
output:> def reverse_keys_values(dict1):
(Pdb) c
{3: 'a', 1: 'b', 2: 'c'}
PS D:\pythonprogramms> & "C:/Users/Yagjna Sri B/AppData/Local/Programs/Python/Python310/python.exe" d:/pythonprogramms/reverse_keys_values.py
> d:\pythonprogramms\reverse_keys_values.py(3)<module>()
-> def reverse_keys_values(dict1):
(Pdb) n
> d:\pythonprogramms\reverse_keys_values.py(10)<module>()
-> dict1 = {'a': 3, 'b': 1, 'c': 2}
(Pdb) n
> d:\pythonprogramms\reverse_keys_values.py(11)<module>()
-> dict2 = reverse_keys_values(dict1)
(Pdb) n
> d:\pythonprogramms\reverse_keys_values.py(13)<module>()
-> print('{}'.format(dict2))
(Pdb) n
{3: 'a', 1: 'b', 2: 'c'}
--Return--
> d:\pythonprogramms\reverse_keys_values.py(13)<module>()->None
-> print('{}'.format(dict2))'''

