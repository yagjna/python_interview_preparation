def to_camel_case(text):
    
    text1 = text.split("-")
    
    return "".join(text1)

text = "The_stealth_worrior"
text1 = to_camel_case(text)

print("the text is : {}".format(text1))

#output:
the text is : The_stealth_worrior
