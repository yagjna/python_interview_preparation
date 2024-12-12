def solution(s):
    
    result = ''
    
    for char in s:
        if char.isupper():  
            result = result+ ' '   
        result = result + char
    
    return result

s = "camelCasing" 
result = solution(s)

print(s)



#output :camel Casing
