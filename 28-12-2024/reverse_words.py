def reverse_words(text):
    
    str1 = text.split(' ')
    lst1 = []
    
    for x in str1:
        y = x[::-1]
        lst1.append(y)
        
    return ' '.join(lst1)

text = "This is an example!"
lst1 = reverse_words(text)
print('the revrsed string is- {}'.format(lst1))


#output:
the revrsed string is- sihT si na !elpmaxe
