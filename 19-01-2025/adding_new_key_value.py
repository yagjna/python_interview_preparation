
def adding(dict1):
    dict1.setdefault('c', 3)

    return dict1

dict1 = {'a': 1, 'b': 2}

new_dict = adding(dict1)
print(new_dict)

file_name = '19-01-2025.txt'
with open(file_name, "a") as fh:
    fh.write('\n adding new key value pair:\n')
    fh.write(str(new_dict) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
{'a': 1, 'b': 2, 'c': 3}
the file is added to - 19-01-2025.txt
