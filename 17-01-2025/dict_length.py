
def dict_length(dict1):

    dict2 = {}

    for k, v in dict1.items():
        dict2[k] = len(v)

    return dict2

dict1 = {'a': [1, 2], 'b': [3, 4, 5]}
dict2 =  dict_length(dict1)

print(dict2)

file_name = 'list_count.txt'
with open(file_name, 'a') as fh:
    fh.write('\n dict_values_length: \n')
    fh.write(str(dict2) + '\n')

print('the file added to - {}'.format(file_name))

#output:
{'a': 2, 'b': 3}
the file added to - list_count.txt
