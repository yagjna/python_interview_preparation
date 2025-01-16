
def list_count(lst1, lst2):

    lst3 = lst1 + lst2
    dict1 = {}

    for x in lst3:
        if x in dict1:
            dict1[x] = dict1[x] +1
        else:
            dict1[x] = 1

    return dict1

lst1 = ['a', 'a', 'c', 'e']
lst2 = ['c', 'e', 'f', 'g']

lst3 = list_count(lst1, lst2)
print(lst3)

file_name = 'list_count.txt'
with open(file_name, 'w') as fh:
    fh.write(str(lst3))

print("the list_count file is added to - {}".format(file_name))

