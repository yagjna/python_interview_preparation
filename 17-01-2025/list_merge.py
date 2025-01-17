
def merge(lst1, lst2):
    dict1= {}

    x = 0
    for i in lst1:
        dict1[i] = lst2[x]
        x = x + 1

    return dict1

lst1 = ['a', 'b', 'c', 'd']
lst2 = ['x', 'y', 'z', 'p']
dict1 = merge(lst1, lst2)

print(dict1)

file_name = 'list_count.txt'
with open(file_name, 'a') as fh:
    fh.write('\n list merge:\n')
    fh.write(str(dict1)+ '\n')

print('the file added to - {}'.format(file_name))

#output:
{'a': 'x', 'b': 'y', 'c': 'z', 'd': 'p'}
the file added to - list_count.txt
