
def palindrome(str1):
    str2 = str1[::-1]

    if str1 == str2:
        return 'string is palindrome'

    else:
        return 'string is not palindrome'

str1 = eval(input('enter a string:'))

print(palindrome(str1))

file_name = 'palindrome.txt'

with open(file_name, 'w') as fh:
    fh.write("{}/n".format(str1))


