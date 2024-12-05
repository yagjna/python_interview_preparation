def remove_multiple(lst1, lst2):

    lst3 = []

    for x in lst1:
        if x not in lst2:
            lst3.append(x)
            
    return lst3

lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = [3,5,7]

lst3 = remove_multiple(lst1,lst2)

print('the list after removing multiple elements is : {}'.format(lst3))


# output :
the list after removing multiple elements is : [1, 2, 4, 6, 8, 9, 10]
