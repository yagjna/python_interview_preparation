
def factorial(number):

    fact = 1

    for x in range(1, number+1):
        fact = fact * x

    return fact

number = eval(input('enter a number : '))
fact =  factorial(number)

print('the factorial of {} is - {}'.format(number, fact))

#output:
enter a number : 5
the factorial of 5 is - 120
