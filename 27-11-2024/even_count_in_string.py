def even(str1):
    lst1 = str1.split()
    lst2 = []
    for x in lst1:
        if len(x) % 2 == 0:
            lst2.append(x)
    return lst2
str1 = eval(input("enter a string:"))
x = even(str1)
print(x)




output:
    enter a string:"this is a string"
['this', 'is', 'string']
