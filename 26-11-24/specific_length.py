def length(lst1):
    lst2 = []
    length = 3
    for x in lst1:
        if len(x)== length:
            lst2.append(x)
    return lst2
lst1 = ['cat', 'dog', 'elephant','donkey', 'rat']
lst2 = length(lst1)
print('the words with length 3 are {}' .format(lst2))


output:
    the words with length 3 are ['cat', 'dog', 'rat']




