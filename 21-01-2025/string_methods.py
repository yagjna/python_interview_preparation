
str1 = 'abc'
str2 = '123'

# concatination of 2 stings
print(str1 + str2)
print('{}'.format(str1 + str2))



#splitting a string using seperator (string to list)
str3 = 'this is a sting'
print(str3.split(' '))
print('{}'.format(str3.split(' ')))



#joining of list of strings using a seperator (list to sting)
print(''.join(str3))
print('{}'.format(''.join(str3)))



#to remove empty spaces in the string
str1 = '   this is a elephant  '
print(str1.strip())
#to remove empty spaces at the left of string
print('{}'.format(str1.lstrip()))
#to remove empty spaces at right of string
print('{}'.format(str1.rstrip()))


#to change letters of string to upper case
str1 = 'this is fan'
print(str1.upper())

#to capitalize the first letter of string
print(str1.capitalize())

#to capitalize each and every first letter of string
print(str1.title())

#output:
bc123
abc123
['this', 'is', 'a', 'sting']
['this', 'is', 'a', 'sting']
this is a sting
this is a sting
this is a elephant
this is a elephant
   this is a elephant
THIS IS FAN
This is fan
This Is Fan
