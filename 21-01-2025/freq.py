
def frequency_of_charcter(str1):

    dict1 = {}

    for x in str1:
        if x in dict1:
            dict1[x] = dict1[x] + 1
        else:
            dict1[x] = 1

    return dict1

str1 = 'aabbccdeef'
dict1 = frequency_of_charcter(str1)

print('the frequency of each character in the dictionary is - {}'.format(dict1))

#output:
the frequency of each character in the dictionary is - {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 2, 'f': 1}
