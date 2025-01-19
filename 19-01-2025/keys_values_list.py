
def key_value_list(dict1):

    keys = []
    values = []

    for k, v in dict1.items():
        keys.append(k)
        values.append(v)

    return keys, values

dict1 =  {'a': 1, 'b': 2}
keys, values = key_value_list(dict1)

print('{}',format(keys))
print('{}'.format(values))

file_name = '19-01-2025.txt'
with open(file_name, "a") as fh:
    fh.write('\n keys and values lists:\n')
    fh.write(str(keys) + '\n')
    fh.write(str(values) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
keys = {} ['a', 'b']
values = [1, 2]
the file is added to - 19-01-2025.txt
