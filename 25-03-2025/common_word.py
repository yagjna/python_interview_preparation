
import pdb;pdb.set_trace()

def common_words(str1):
    str2 = str1.split(' ')
    lst1 = []
    dict1 = {}
    for x in str2:
        if x in dict1:
            dict1[x] = dict1[x] + 1
        else:
            dict1[x] = 1

    for k, v in dict1.items():
        if v > 1:
            lst1.append(k)

    return lst1

str1 = "this is a test this is only a test"
lst1 = common_words(str1)

print('the common words in the string - {}'.format(lst1))

"""
output:> d:\pythonprogramms\common_words_in_string.py(3)<module>()
-> def common_words(str1):
(Pdb) n
> d:\pythonprogramms\common_words_in_string.py(19)<module>()
-> str1 = "this is a test this is only a test"
(Pdb) n
> d:\pythonprogramms\common_words_in_string.py(20)<module>()
-> lst1 = common_words(str1)
(Pdb) n
> d:\pythonprogramms\common_words_in_string.py(22)<module>()
-> print('the common words in the string - {}'.format(lst1))
(Pdb) n
the common words in the string - ['this', 'is', 'a', 'test']
> d:\pythonprogramms\common_words_in_string.py(24)<module>()
-> """





