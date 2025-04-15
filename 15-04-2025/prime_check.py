
def prime_composite(number):

    if number == 2:
        return 'neither prime not composite'

    lst1 = []

    for x in range(1, number + 1):
        if number % x == 0:
            lst1.append(x)

    if len(lst1) == 2:
        return 'the number is prime'
    else:
        return 'the number is not prime'

number = eval(input('enter a number : '))
result = prime_composite(number)

print('{}'.format(result))

'''output:enter a number : 2
neither prime not composite
enter a number : 5
the number is prime
enter a number : 6
the number is not prime'''

