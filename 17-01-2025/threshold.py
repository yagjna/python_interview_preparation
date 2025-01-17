
def threshold(dict1, value):

    dict2 = {}
    for k, v in dict1.items():
        if v > value:
            dict2[k] = v

    return dict2

dict1 = {'a': 5, 'b': 18, 'c': 11, 'd': 3}
value = eval(input('enter a value: '))

dict2 = threshold(dict1, value)
print(dict2)

file_name = 'list_count.txt'
with open(file_name, 'a') as fh:
    fh.write('\n threshold dictory is : \n')
    fh.write(str(dict2) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
enter a value: 9
{'b': 18, 'c': 11}
