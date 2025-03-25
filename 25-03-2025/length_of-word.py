
import pdb;pdb.set_trace()

def length_of_words(str1):

    str2 = str1.split(' ')
    dict1 = {}
    for x in str2:
        dict1[x] = len(x)

    return dict1

str1 = "hello world python"
dict1 = length_of_words(str1)

print('the length of each word in the string is - {}'.format(dict1))


'''
d:\pythonprogramms\leng_of_word.py(3)<module>()
-> def length_of_words(str1):
(Pdb) n
> d:\pythonprogramms\leng_of_word.py(12)<module>()
-> str1 = "hello world python"
(Pdb) n
> d:\pythonprogramms\leng_of_word.py(13)<module>()
-> dict1 = length_of_words(str1)
(Pdb) n
> d:\pythonprogramms\leng_of_word.py(15)<module>()
-> print('the length of each word in the string is - {}'.format(dict1))
(Pdb) n
the length of each word in the string is - {'hello': 5, 'world': 5, 'python': 6}
--Return--
> d:\pythonprogramms\leng_of_word.py(15)<module>()->None
-> print('the length of each word in the string is - {}'.format(dict1))
'''
