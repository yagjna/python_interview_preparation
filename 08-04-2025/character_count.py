
def character_count(str1):

    dict1 = {}
    for x in str1:
        if x in dict1:
            dict1[x] = dict1[x] + 1
        else:
            dict1[x] = 1

    lst1 = []
    for k, v in dict1.items():
        lst1.append(str(k)+str(v))

    return ''.join(lst1)

str1 = "aaabbcc"
lst1 = character_count(str1)

print(lst1)

#output:a3b2c2
