def vowels(str1):
    vowels = "aeiouAEIOU"
    dict1 = {}
    for x in str1:
        if x in vowels:
            if x in dict1:
                dict1[x] = dict1[x]+1
            else:
                dict1[x] = 1
    sum = 0
    for k,v in dict1.items():
        sum = sum + v
        # print("the total no of vowels is {}".format(sum))
    return sum
str1 = eval(input("enter a string :"))
x = vowels(str1)
print("the total no of vowels is {}".format(x))




output:
    enter a string :'abcedefghijklmnopqrstuvwxyz'
the total no of vowels is 6
