def clean_string(s):
    y = []
    for x in s:
        if x.isalpha():  
            y.append(x)
            
    return ''.join(y)

s = 'abc#d##c'
print(clean_string(s))  

#output:
abcdc
