def factorial(number):
    fact = 1

    for x in range(1, number+1):
        fact = fact * x

    return fact

number =5
print(factorial(number))

#output:
120
