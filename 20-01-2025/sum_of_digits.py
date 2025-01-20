
def sum_of_digits(num):

    result = 0

    while num != 0:
        reminder = num % 10
        num = num // 10
        result = result + reminder

    return result

num = eval(input('enter a number:'))
result = sum_of_digits(num)

print('the sum is : {}'.format(result))

file_name = '20-01-2025.txt'

with open(file_name, 'a') as fh:
    fh.write('\n sum of digits is:\n')
    fh.write(str(result) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
enter a number:1234
the sum is : 10
the file is added to - 20-01-2025.txt
