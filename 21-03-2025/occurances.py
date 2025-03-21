
#Write a Python program to count occurrences of each word in a given string.

def occurances_of_word(str1):

    dict1 = {}

    for x in str1:
        if x in dict1:
           dict1[x] = dict1[x] +1

        else:
            dict1[x] = 1

    return dict1

str1 = 'aabbc'
print(occurances_of_word(str1))

output:
    {'a': 2, 'b': 2, 'c': 1}
