def number(lines):
    
    dict1 = {}
    
    for index, element in enumerate(lines, start=1):
        dict1[index] = element  
    
    result = []

    for key, value in dict1.items():
        str1 = str(key) + ": " + str(value)
        result.append(str1)
    
    return result

lines = ["a", "b", "c"]
lst = number(lines)

print(lst)



#output:
['1: a', '2: b', '3: c']
