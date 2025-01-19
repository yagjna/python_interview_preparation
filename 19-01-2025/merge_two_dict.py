def merge(dict1, dict2):

    dict1.update(dict2)

    return dict1

dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}

merged_dict = merge(dict1, dict2)

print("{}".format(merged_dict))

file_name = '19-01-2025.txt'
with open(file_name, "a") as fh:
    fh.write('\n merged dictionary:\n')
    fh.write(str(merged_dict) + '\n')

print('the file is added to - {}'.format(file_name))


#output:
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
the file is added to - 19-01-2025.txt
