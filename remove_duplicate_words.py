def remove_duplicate_words(s):
    
    str1 = s.split()
    lst1 = []
    for x in str1:
        if x not in lst1:
            lst1.append(x)
    return ' '.join(lst1)

s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
str1 =  remove_duplicate_words(s)

print(str1)


#output:

alpha beta gamma delta
