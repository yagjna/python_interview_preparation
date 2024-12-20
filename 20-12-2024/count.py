def count(s):
    dict1 = {}
    
    for x in s:
        if x in dict1:
            dict1[x] = dict1[x] + 1
            
        elif x not in dict1:
            dict1[x] = 1
        else:
            dict1 = {}
            
    return dict1

s = 'aba'
dict1 = count(s)

print(dict1)


#output:
{'a': 2, 'b': 1}
