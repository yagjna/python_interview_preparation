
str1 = "abcdef"

print(id(str1))

str1 = str1 + "g"

print(id(str1))

print(str1[5:])
print(id(str1))

str1 = str1[5:]
print(str1)
print(id(str1))

#output:
2289718473456
2289718474160
fg
2289718474160
fg
2289718470320
