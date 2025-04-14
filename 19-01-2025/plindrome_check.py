
def palindrome(str1):

    str2 = str1[::-1]

    if str2 == str1:
        return True
    else:
        return False

str1 = eval(input('enter a string:'))

str2 = palindrome(str1)

print('{}'.format(str2))

file_name = '19-01-2025.txt'
with open(file_name, "a") as fh:
    fh.write('\n plindrome chek:\n')
    fh.write(str(str2) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
enter a string:'madam'
True
the file is added to - 19-01-2025.txt

enter a string:'abcd'
False
the file is added to - 19-01-2025.txt
