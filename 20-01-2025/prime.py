
def prime_number(number):

    lst1 = []

    for x in range(1, number+ 1):
        if number % x == 0:
            lst1.append(x)

    if len(lst1) == 2:
        return 'the number is prime {}'.format(number)
    else:
        return 'the number is composite {}'.format(number)

number = eval(input('enter a number :'))
result = prime_number(number)

print('{}'.format(result))

file_name = '20-01-2025.txt'

with open(file_name, 'a')as fh:
    fh.write('\n prime or composite:\n')
    fh.write(str(result) + '\n')

print('the file is added to - {}'.format(file_name))

#output:
enter a number :5
the number is prime 5
the file is added to - 20-01-2025.txt

enter a number :10
the number is composite 10
the file is added to - 20-01-2025.txt
