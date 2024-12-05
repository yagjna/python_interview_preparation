def duplicates_product(lst1):

    lst2 = []
    product = 1

    for x in lst1:
        if x not in lst2:
            lst2.append(x)
            product = product *x

    return product

lst1 = [1,1,2,2,3,4,5]
product = duplicates_product(lst1)
print('the product after removing duplicates is - {}'.format(product))







#output :
the product after removing duplicates is - 120
