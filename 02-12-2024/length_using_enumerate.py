str1 = 'hqllo world'
dict1 = {}
str2 =str1.split(' ')
for index,element in enumerate(str2):
   dict1[element] = len(element)
print(dict1)




output :
    {'hqllo': 5, 'world': 5}
