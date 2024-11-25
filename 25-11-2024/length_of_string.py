#wap to take list of strings and create a dict in which keys are the strings and the values are the length of those strings.


def length_of_strings(lst1):

    dict1 = {}

    for x in lst1:
            dict1[x] = len(x)
    return dict1

lst1 = ['apple','banana','cherry']
dict1 = length_of_strings(lst1)

print("the length of each string in the list is : {}".format(dict1))


output :the length of each string in the list is : {'apple': 5, 'banana': 6, 'cherry': 6}
