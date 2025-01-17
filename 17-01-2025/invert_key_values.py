
def invert_key_value(dict1):
    dict2 = {}

    for k, v in dict1.items():
        dict2[v] = k

    return dict2

dict1 = {1: 'a', 2: 'b'}
dict2 = invert_key_value(dict1)

print(dict2)

file_name = 'list_count.txt'
with open(file_name, 'a') as fh:
    fh.write('\n invert key values:\n')
    fh.write(str(dict2)+ '\n')

print('the file is added to - {}'.format(file_name))

#output:
{'a': 1, 'b': 2}
