
def camel_case(str1):
    str2 = str1.split('_')

    words = []
    for x in str2:
       y = x[0].upper() + x[1:].lower()
       words.append(y)
    return ''.join(words)

str1 = "this_is_a_test"
lst1 = camel_case(str1)

print('the string after converting to camel case is -{}'.format(lst1))

file_name = "list_count.txt"
with open(file_name, 'a') as fh:
    fh.write('\n camel case:\n')
    fh.write(str(lst1) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
the string after converting to camel case is -ThisIsATest
the file is added to - list_count.txt
