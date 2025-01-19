
#using temp variable
def swap_numbers(a, b):
    
    temp = a
    a = b
    b = temp

    return a, b

a =1 
b =2

a, b = swap_numbers(a, b)

print('a = {}'.format(a))
print('b = {}'.format(b))

file_name = '19-01-2025.txt'
with open(file_name, "a") as fh:
    fh.write('\n swap numbers:\n')
    fh.write(str(a) + '\n')
    fh.write(str(a) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
a = 2
b = 1
the file is added to - 19-01-2025.txt

#without using temp variable
def swap_numbers(a, b):

    a = a + b
    b = a -b
    a = a -b
    return a, b
a =1
b =2

a, b = swap_numbers(a, b)

print('a = {}'.format(a))
print('b = {}'.format(b))

file_name = '19-01-2025.txt'
with open(file_name, "a") as fh:
    fh.write('\n swap numbers:\n')
    fh.write(str(a) + '\n')
    fh.write(str(a) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
a = 2
b = 1
the file is added to - 19-01-2025.txt

