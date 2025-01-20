def reverse_digits(number):
    result = 0

    while number != 0:
        reminder = number % 10
        number = number // 10
        result = result*10 + reminder

    return result

number = 1234
print(reverse_digits(number))


#output:
4321
