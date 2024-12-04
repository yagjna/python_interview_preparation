
def check_substring(str1, substring):

    if substring in str1:
        print('Yes, it is a substring.')
    else:
        print('No, it is not a substring.')


str1 = input('Enter a string: ')
substring = input('Enter a substring: ')
check_substring(str1, substring)

#output: Enter a string: 'hello world'
Enter a substring: 'hello'


