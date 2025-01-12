
def largest_number(num1, num2):

    if num1 > num2:
        return '{} is largest'.format(num1)

    else:
        return '{} is largest'.format(num2)

num1 = eval(input('enter a number : '))
num2 = eval(input('enter a number : '))

result = (largest_number(num1, num2))
print(result)
file_name = 'largest_number.txt'
with open(file_name, 'w') as fh:
    fh.write(result)
