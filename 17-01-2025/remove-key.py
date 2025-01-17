
def remove_key(dict1):

    if key in dict1:
        dict1.pop(key)
    else:
        return "the key is not present in dictionary"

    return dict1

dict1 = {'a':1, "b":2, 'c':3}
key = eval(input('enter a key:'))

dict2 = remove_key(dict1)
print(dict2)

file_name = 'list_count.txt'
with open(file_name, 'a') as fh:
    fh.write('\n remove key without error: \n')
    fh.write(str(dict2) + '\n')

print('the file added to - {}'.format(file_name))

#output:
enter a key:'a'
{'b': 2, 'c': 3}
the file added to - list_count.txt

enter a key:'z'
the key is not present in dictionary
the file added to - list_count.txt
