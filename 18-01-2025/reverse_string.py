
def reverse_string(str1):
    reversed_str = ''
    for x in str1:
        reversed_str = x + reversed_str

    return reversed_str

str1 = "abcd"
reversed_str1 = reverse_string(str1)

print("the resversed string is - {}".format(reversed_str1))

file_name = "list_count.txt"
with open(file_name, 'a') as fh:
    fh.write('\nreversed string:\n')
    fh.write(str(reversed_str1) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
the resversed string is - dcba
the file is added to - list_count.txt
