def least_freq_char(str1):
    
    dict1 = {}

    for x in str1:
        if x in dict1:
            dict1[x] = dict1[x] + 1
        else:
            dict1[x] = 1

    for k, v in dict1.items():
        if v == 1:
            return k


str1 = 'helloworldhowareyou'

k = least_freq_char(str1)

print(' the least freq character is : {}'.format(k))



#output: the least freq character is : d
