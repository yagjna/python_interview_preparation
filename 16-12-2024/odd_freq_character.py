def odd_freq_character(str1):
    lst1 = []
    dict1 = {}

    for x in str1:
        if x in dict1:
            dict1[x] = dict1[x] +1 
        else:
            dict1[x] = 1

    for k, v in dict1.items():
        if v %2 != 0:
            lst1.append(k)

    return lst1


str1 = 'helloworldhowareyou'
lst1 = odd_freq_character(str1)

print(lst1)



#output: ['l', 'd', 'a', 'y', 'u']
