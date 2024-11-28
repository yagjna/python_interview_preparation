def length(str1):
    dict1 ={}
    str2 = str1.split()
    for x in str2:
        dict1[x] = len(x)
    return dict1
str1 = "geeks for geeks is"
dict1 = length(str1)
print(dict1)



output:
    {'geeks': 5, 'for': 3, 'is': 2}
