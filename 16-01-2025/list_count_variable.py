
def list_count_variables(lst1, lst2):
    lst3 = lst1 + lst2
    dict1 = {}

    for x in lst3:
        if x in dict1:
            dict1[x] = dict1[x] + 1
        else:
            dict1[x] = 1

    return dict1

lst1 = ['a', 'b', 'c', 'a', 'a']
lst2 = ['b', 'c']
lst3 = list_count_variables(lst1, lst2)

print('The variable count is - {}'.format(lst3))

file_name = 'list_count.txt'
with open(file_name, 'a') as fh:
    fh.write('\n count_of_variables \n')
    fh.write(str(lst3) + '\n')

print('the file is added to - {}'.format(file_name))
