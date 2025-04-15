
str1 = "this is a dog"

lst1 = str1.split()

print(lst1)

# to find the length
for x in lst1:
    print("the length of {} is {}".format(x,len(x)))


'''
output:
    ['this', 'is', 'a', 'dog']
the length of this is 4
the length of is is 2
the length of a is 1
the length of dog is 3'''
