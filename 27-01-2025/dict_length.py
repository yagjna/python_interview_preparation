
def dict_length(dict1):

    dict2 = {}

    for k, v in dict1.items():
        dict2[k] = len(v)

    return dict2

dict1 = {'a': [1, 2], 'b': [3, 4, 5]}
dict2 =  dict_length(dict1)

print(dict2)

#output:
{'a': 2, 'b': 3}
