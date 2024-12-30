def capitals(word):
    lst1 = []
    for i, x in enumerate(word):
        if x.isupper():
            lst1.append(i)
    
    return lst1
            
word = "CodEWaRs"
print(capitals(word))
            
#output:
[0, 3, 4, 6]
