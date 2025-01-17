
def frequency_of_char(lst1):

    dict1 = {}

    for x in lst1:
            dict1[x]= dict1.get(x, 0) +1

    return dict1

lst1 = ['a','a','b','d']
dict1 = frequency_of_char(lst1)

print(dict1)

#output:
{'a': 2, 'b': 1, 'd': 1}
