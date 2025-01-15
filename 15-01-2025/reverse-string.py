
def palindrome_check(str1):
    str2 = str1[::-1]

    if str1 == str2:
        return 'The string is a palindrome'
    else:
        return 'The string is not a palindrome'

str1 = input('Enter a string: ')
print(palindrome_check(str1))

#output:
Enter a string: 'iagdilgeldbadglcueh'
The string is not a palindrome

Enter a string: 'madam'
The string is a palindrome
