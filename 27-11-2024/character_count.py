def char(str1):
    dict1 = {}
    for x in str1:
        if x in dict1:
            dict1[x] = dict1[x] +1
        else:
            dict1[x] = 1
    output = ''
    for k,v in dict1.items():
        output = output + str(k) + str(v)
    return output
str1 = 'ABAABBCA'
output = char(str1)
print(output)


output: 
    A4B3C1
