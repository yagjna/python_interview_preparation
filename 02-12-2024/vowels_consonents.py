
def vowels_consonents(str1):
    dict1 = {'vowels':[], 'consonents':[]}
    vowels = 'aeiouAEIOU'
    for x in str1:
        if x in vowels:
            dict1['vowels'].append(x)
        else:
            dict1['consonents'].append(x)
    return dict1

str1 = 'abcdefghijklmnopqrstuvwxyz'
dict1 = vowels_consonents(str1)
print('the vowels and consonents are : {}'.format(dict1))



# output : the vowels and consonents are : {'vowels': ['a', 'e', 'i', 'o', 'u'], 'consonents': ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']}
