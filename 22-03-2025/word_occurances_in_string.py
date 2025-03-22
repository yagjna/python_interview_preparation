
import pdb;pdb.set_trace()

def word_occurances(str1):

    str2 = str1.split(' ')

    dict1 = {}

    for x in str2:
        if x in dict1:
            dict1[x] = dict1[x] +1
        else:
            dict1[x] = 1

    return dict1

str1 = 'this is string this is'
dict1 =  word_occurances(str1)

print('the occurances of each word in the string is - {}'.format(dict1))

#output:
d:\pythonprogramms\word_occurances_in_sentence.py(3)<module>()
-> def word_occurances(str1):
(Pdb) n
> d:\pythonprogramms\word_occurances_in_sentence.py(17)<module>()
-> str1 = 'this is string this is'
(Pdb) n
> d:\pythonprogramms\word_occurances_in_sentence.py(18)<module>()
-> dict1 =  word_occurances(str1)
(Pdb) n
> d:\pythonprogramms\word_occurances_in_sentence.py(20)<module>()
-> print('the occurances of each word in the string is - {}'.format(dict1))
(Pdb) print(dict1)
{'this': 2, 'is': 2, 'string': 1}
(Pdb) c
the occurances of each word in the string is - {'this': 2, 'is': 2, 'string': 1}    
