
def factorial(number):

    if number == 0:
        result = 1
    else:
        result = number * factorial(number - 1)

    return result

number = eval(input('enter a number :'))
result = factorial(number)

print('the factorial of number is - {}'.format(result))

''' output :
    enter a number :5
the factorial of number is - 120'''
