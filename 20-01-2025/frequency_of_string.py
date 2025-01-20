
def freq_of_string(str1):

    dict1 = {}

    for x in str1:
        if x in dict1:
            dict1[x] = dict1[x] + 1

        else:
            dict1[x] = 1

    return dict1
str1 = 'aabbccd'

dict1 = freq_of_string(str1)

print('the frequency of each character is - {}'.format(dict1))

file_name = '20-01-2025.txt'

with open(file_name, 'a') as fh:
    fh.write('\n the frequency of string is:\n')
    fh.write(str(dict1) + '\n')


print('the file is added to - {}'.format(file_name))

#output:
the frequency of each character is - {'a': 2, 'b': 2, 'c': 2, 'd': 1}
the file is added to - 20-01-2025.txt
