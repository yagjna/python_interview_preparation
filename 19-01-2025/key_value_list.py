
def key_value(keys, values):

    dict1 = {}
    for x in keys:
        dict1[x] = values

    return dict1

keys = ['a', 'b']
values = [1, 2, 3]
dict1 = key_value(keys, values)

print("{}".format(dict1))

file_name = '19-01-2025.txt'
with open(file_name, "w") as fh:
    fh.write('\n key_value_list:\n')
    fh.write(str(dict1) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
{'a': [1, 2, 3], 'b': [1, 2, 3]}
the file is added to - 19-01-2025.txt
