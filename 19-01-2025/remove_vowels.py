
def remove_vowels(str1):
    vowels = 'aeiouAEIOU'
    lst1 = []

    for x in str1:
        if x not in vowels:
            lst1.append(x)

    return ''.join(lst1)

str1 = 'hello world'
lst1 = remove_vowels(str1)

print(lst1)

file_name = '19-01-2025.txt'
with open(file_name, "a") as fh:
    fh.write('\n remove vowels:\n')
    fh.write(str(lst1) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
hll wrld
the file is added to - 19-01-2025.txt
