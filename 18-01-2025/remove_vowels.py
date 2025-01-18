
def remove_vowels(str1):
    vowels = 'aeiouAEIOU'
    lst1 = []
    for x in str1:
        if x not in vowels:
            lst1.append(x)

    return ''.join(lst1)

str1 = 'elephant'
result = remove_vowels(str1)

print('the string without vowels is - {}'.format(result))


file_name = "list_count.txt"
with open(file_name, 'a') as fh:
    fh.write('\nKey-value pairs:\n')
    fh.write(str(result))

print('the file is added to - {}'.format(file_name))

#output:
the string without vowels is - lphnt
the file is added to - list_count.txt
