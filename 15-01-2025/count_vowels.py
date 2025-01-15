
def count_vowels(str1):

    vowels = 'aeiouAEIOU'
    dict1 = {}

    for x in str1:
        if x in vowels:
            if x in dict1:
                dict1[x] = dict1[x] + 1

            else:
                dict1[x] = 1


    return dict1

str1 = eval(input('enter a string : '))

print(count_vowels(str1))

#output:
enter a string : 'iqwgtedilgbwaiuhdgiweuhufd;o'
{'i': 4, 'e': 2, 'a': 1, 'u': 3, 'o': 1}
