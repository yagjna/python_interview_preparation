
str1 = eval(input("enter a string:"))

vowels = "aeiouAEIOU"
#consonents = "bcdfghjklmnpqrstuvwxyz"

import pdb;pdb.set_trace()

dir1 = {"vowels_count":{},"consonents_count":{}}

for x in str1:
    if x not in vowels:
        dir1["consonents_count"][x]=dir1.get(x,1)
        import pdb;pdb.set_trace()
    else:
        dir1["vowels_count"][x] = dir1["vowels_count"][x] + 1


print(dir1)

