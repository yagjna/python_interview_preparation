
def palindrome(str1):
    str2 = str1[::-1]

    if str1 == str2:
        return 'string is palindrome'
    
    else:
        return 'string is not palindrome'

str1 = eval(input('enter a string:'))

print(palindrome(str1))

''' enter a string:'madam'
string is palindrome
'''
