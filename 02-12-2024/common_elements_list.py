lst1 = [1,2,3,4,4]
lst2 =[4,4,5,6]
dict1 ={}
for x in lst1:
    if x in lst2:
     if x in dict1:
        dict1[x] = dict1[x]+1
     else:
        dict1[x] =1

print(dict1)




#output:{4: 2}
