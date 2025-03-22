
import pdb;pdb.set_trace()

def vowels_consonants(text):
    vowels = 'aeiouAEIOU'
    dict1 = {}

    for x in text:
        if x.isalpha():
            dict1[x] = dict1.get(x, 0) + 1
    return dict1

text = 'text'
print(vowels_consonants(text))


'''
output: d:\pythonprogramms\count_vowels_consonents.py(3)<module>()
-> def vowels_consonants(text):
(Pdb) n
> d:\pythonprogramms\count_vowels_consonents.py(12)<module>()
-> text = 'text'
(Pdb) n
> d:\pythonprogramms\count_vowels_consonents.py(13)<module>()
-> print(vowels_consonants(text))
(Pdb) c
{'t': 2, 'e': 1, 'x': 1}

'''
