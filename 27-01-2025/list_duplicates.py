
def remove_duplicates(lst1):

    lst2 = []

    for x in lst1:
        if x not in lst2:
            lst2.append(x)

    return lst2

lst1 = [1, 2, 3, 4, 1, 3, 2, 5]
lst2 = remove_duplicates(lst1)

print('the list after removing duplicates is - {}'.format(lst2))


#output:
the list after removing duplicates is - [1, 2, 3, 4, 5]
