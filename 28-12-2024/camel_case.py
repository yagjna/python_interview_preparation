def camel_case(s):
    # Split the string into words
    str1 = s.split(' ')
    lst1 = []

    for x in str1:
        if x:  # Avoid empty strings caused by multiple spaces
            # Capitalize the first letter and keep the rest as is
            y = x.capitalize()
            lst1.append(y)
    
    # Join all words without spaces to form camelCase
    return ''.join(lst1)

# Test case
s = "hello case"
print(camel_case(s))  # Output: "HelloCase"

s = "camel case method"
print(camel_case(s))  # Output: "CamelCase"


#output:
HelloCase
CamelCaseMethod
