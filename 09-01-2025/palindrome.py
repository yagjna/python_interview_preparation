
def palindrome(str1):
    str2 = str1[::-1]

    if str2 == str1:
        return 'palindrome'
    else:
        return 'not palindrome'

str1 = 'madam'

print(palindrome(str1))
