def reverse_letter(st):
    
    str2 = ''
    
    for x in st:
        if x.isalpha():  
            str2 += x  
    str1 = str2[::-1]  
    return str1


st = "ultr53o?n"
str1 = reverse_letter(st)

print(' the reversed string is : {}'.format(str1))

#output:
the reversed string is : nortlu
