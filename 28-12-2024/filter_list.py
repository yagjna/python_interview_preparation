def filter_list(l):
    
    lst1 = []
    
    for x in l:
        if type(x) == int:
            lst1.append(x)
            
    return lst1

l = ([1,2,'a','b'])
print(filter_list(l))

l = ([1,'a','b',0,15])
print(filter_list(l))

l = ([1,2,'aasf','1','123',123])
print(filter_list(l))
    



#output:
[1, 2]
[1, 0, 15]
[1, 2, 123]
