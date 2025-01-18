
def anargs(str1, str2):

    for x in str1:
        for x in str2:
            if x in str1 and str2:
                return True
            else:
                return False

str1= 'listen'
str2 = 'silent'

str3 = anargs(str1, str2)
print(str3)

str1 = 'hello'
str2 = 'world'

str3 = anargs(str1, str2)
print(str3)

file_name = "list_count.txt"
with open(file_name, 'a') as fh:
    fh.write('\nreversed string:\n')
    fh.write(str(str3) + '\n')

print('the file is added to - {}'.format(file_name))

#output;
True
False
the file is added to - list_count.txt
