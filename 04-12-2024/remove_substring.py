def substring(str1,str2):
    str3 = str1.split(' ')
    str4 = str2.split(" ")
    lst1 = []
    for x in str3:
        if x not in str4:
            lst1.append(x)
    return ' '.join(lst1)

str1 = eval(input('enter a string : '))
str2 = eval(input('enter a substring : '))
str3 = substring(str1,str2)
print(str3)



#output:
enter a string : 'this is python, i love python'
enter a substring : 'python is'
this python, i love
