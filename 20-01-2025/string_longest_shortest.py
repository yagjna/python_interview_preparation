
def longest_shortest_string(str1):
    str2 = str1.split(' ')
    long = str2[0]
    small = str2[0]

    for x in str2:
        if len(x) > len(long):
            long = x

        if len(x) < len(small):
            small = x

    return long, small

str1 = 'this is a elephant'
long, small = longest_shortest_string(str1)

print('the longest string is - {}'.format(long))
print('the smallest string is -{}'.format(small))

file_name = '20-01-2025.txt'

with open(file_name, 'w') as fh:
    fh.write('\n smallest and longest string:\n')
    fh.write(str(long) + '\n')
    fh.write(str(small) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
the longest string is - elephant
the smallest string is -a
the file is added to - 20-01-2025.txt
