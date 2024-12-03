
def amstrong(number):
    # Initialize result to store the sum of cubes of digits
    result = 0
    temp = number  # Store the original number

    while number != 0:
        reminder = number % 10  # Extract the last digit
        number = number // 10   # Remove the last digit
        result += reminder ** 3  # Add the cube of the digit to result

    if result == temp:
        print('The number is an Armstrong number - {}'.format(temp))
    else:
        print('The number is not an Armstrong number - {}'.format(temp))


number = int(input('Enter a number: '))
amstrong(number)


#output :
Enter a number: 153
The number is an Armstrong number - 153


Enter a number: 123
The number is not an Armstrong number - 123

