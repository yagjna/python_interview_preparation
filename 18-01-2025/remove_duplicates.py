
def duplicate(str1):

    lst1 = []

    for x in str1:
        if x not in lst1:
            lst1.append(x)

    return ''.join(lst1)

str1 = 'hello'
lst1 = duplicate(str1)

print('the list after removing duplicates is - {}'.format(lst1))

file_name = "list_count.txt"
with open(file_name, 'a') as fh:
    fh.write('\nKey-value pairs:\n')
    fh.write(str(lst1) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
the list after removing duplicates is - helo
the file is added to - list_count.txt
