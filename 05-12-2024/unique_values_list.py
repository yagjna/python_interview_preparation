def unique(lst1):

    lst2 = []
    count = 0

    for x in lst1:
        if x not in lst2:
            count = count +1
            lst2.append(x)

    return count

lst1 = [1,2,2,3,4,5,5,5,6,7]
lst2 = unique(lst1)
print('the count of unique characters in the list are : {}'.format(lst2))





#output :
the count of unique characters in the list are : 7
