def key_value_pairs(lst1, lst2):
    dict1 = {}
    x = 0 
    for i in lst1:  
        dict1[i] = lst2[x]  
        x = x + 1  
    return dict1  

lst1 = [1, 2 ]
lst2 = ["a", "b", "c", "d"]

dict1 = key_value_pairs(lst1, lst2)


print(dict1)

'''
output : {1: 'a', 2: 'b'}
'''

