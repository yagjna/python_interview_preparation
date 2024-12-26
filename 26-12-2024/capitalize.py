def capitalize(s):
    lst1 = []
    
    
    pattern1 = ""
    pattern2 = ""
    
    for i, x in enumerate(s):
        if i % 2 == 0:
            pattern1 += x.upper()  
            pattern2 += x.lower()  
        else:
            pattern1 += x.lower()  
            pattern2 += x.upper()  
    
    lst1.append(pattern1) 
    lst1.append(pattern2) 
    
    return lst1

s = "abcdef"
lst1 = capitalize(s)
print(lst1)  

#output:
['AbCdEf', 'aBcDeF']
