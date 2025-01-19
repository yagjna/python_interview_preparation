def frequnecy_num(lst1):

    dict1 = {}

    for num in lst1:
        dict1[num] = dict1.get(num, 0) + 1

    return dict1 

lst1 = [1, 2, 2, 3, 3]
print(frequnecy_num(lst1))

file_name = '19-01-2025.txt'
with open(file_name, "a") as fh:
    fh.write('\n frequency of number:\n')
    fh.write(str(lst1) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
{'a': [1, 2, 3], 'b': [1, 2, 3]}
the file is added to - 19-01-2025.txt
