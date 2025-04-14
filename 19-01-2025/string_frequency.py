
def string_frequency(str1):

    dict1 = {}
    for x in str1:
        dict1[x] = dict1.get(x, 0) + 1

    return dict1

str1 = 'hello'
dict1 = string_frequency(str1)

print('{}'.format(dict1))

file_name = '19-01-2025.txt'
with open(file_name, 'a') as fh:
    fh.write('\n string frequency:\n')
    fh.write(str(dict1) + '\n')

print('the file added to - {}'.format(file_name))

#output:
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
the file added to - 19-01-2025.txt
