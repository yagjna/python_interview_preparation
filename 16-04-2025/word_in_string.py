def word_in_string(str1, x):
    if x in str1:
        return '{} - in {}'.format(x, str1)
    else:
        return '{} - not in {}'.format(x, str1)

str1 = "this is a simple test"
x = input('Enter a word: ')

print(word_in_string(str1, x))

'''
output: 
    Enter a word: a
a - in this is a simple test

Enter a word: above
above - not in this is a simple test'''
