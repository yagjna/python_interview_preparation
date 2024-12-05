def freq(lst1,k):

    dict1 = {}
    lst2 = []

    for x in lst1:
        if x in dict1:
            dict1[x] = dict1[x] +1
        else:
            dict1[x] =1

    for keys,values in dict1.items():
        if values > k:
            lst2.append(keys)

    return lst2

lst1 = [4,5,4,4,6,1,2,2,2,2,3,3.4]
k = eval(input("enter a freq : "))

lst2 = freq(lst1,k)

print('the freq greater than {} are {}'.format(k,lst2))



#output :
enter a freq : 2
the freq greater than 2 are [4, 2]


enter a freq : 6
the freq greater than 6 are []
