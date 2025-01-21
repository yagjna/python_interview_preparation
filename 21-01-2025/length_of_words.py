
def length_of_words(str1):

    str2 = str1.split(' ')
    dict1 = {}

    for x in str2:
       dict1[x] = len(x)


    return dict1

str1 = 'this is a string'
dict1 = length_of_words(str1)

print('{}'.format(dict1))

#output:
{'this': 4, 'is': 2, 'a': 1, 'string': 6}
