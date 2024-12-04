def substing_list(lst1,lst2):

    lst3 = []
    for x in lst1:
        if x in lst2:
            lst3.append(x)
    return lst3

lst1 = ['gfg', 'is', 'best']
lst2 = ['i', 'luv', 'gfg', 'its', 'best']
lst3 = substing_list(lst1,lst2)

print(lst3)




#output : 
['gfg', 'best']
