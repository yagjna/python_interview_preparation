def factorial_of_numbers(numbers):
    
    for num in numbers:
        factorial = 1
        for y in range(1, num + 1):
            factorial *= y
        print("The factorial of {} is {}".format(num, factorial))

        
numbers = [2, 3, 4, 5]
factorial_of_numbers(numbers)




output:
    The factorial of 2 is 2
The factorial of 3 is 6
The factorial of 4 is 24
The factorial of 5 is 120
