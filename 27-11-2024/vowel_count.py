def vowel(str1):
    vowels = 'aeiouAEIOU'
    dict1 = {}
    for x in str1:
        if x in vowels:  # Check if the character is a vowel
            if x in dict1:
                dict1[x] += 1
            else:
                dict1[x] = 1
    for k, v in dict1.items():
        print("{} - occurs {} times".format(k, v))
    return dict1

str1 = "aaAfuiqYWUIEYRkjsdfyu"
vowel(str1)



output:
    a - occurs 2 times
A - occurs 1 times
u - occurs 2 times
i - occurs 1 times
U - occurs 1 times
I - occurs 1 times
E - occurs 1 times
