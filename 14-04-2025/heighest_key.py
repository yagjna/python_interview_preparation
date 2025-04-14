
def heighest_key(dict1):

    longest_key = list(dict1.keys())[0]

    for k, v in dict1.items():
        if v > dict1[longest_key]:
            longest_key = k

    return longest_key

dict1 = {'a': 1235, 'b': 18, 'c': 111}
k = heighest_key(dict1)

print('The key with the highest value is: {}'.format(k))

#output:The key with the highest value is: a
