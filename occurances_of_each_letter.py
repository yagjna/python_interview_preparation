
import pdb;pdb.set_trace()

def occurances_of_each_letter(str1):

    dict1 = {}
    for x in str1:
        if x in dict1:
            dict1[x] = dict1[x] + 1
        else:
            dict1[x] = 1

    return dict1

str1 = eval(input('enter a string:'))
dict1  = occurances_of_each_letter(str1)

print('the occurances of each letter in the string : {}'.format(dict1))

'''
output: -> def occurances_of_each_letter(str1):
(Pdb) n
> d:\pythonprogramms\occurances_of_each_letter.py(14)<module>()
-> str1 = eval(input('enter a string:'))
(Pdb) c
enter a string:'hello'
the occurances of each letter in the string : {'h': 1, 'e': 1, 'l': 2, 'o': 1}
'''
