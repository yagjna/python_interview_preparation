def reverse_num(number):

    result = 0

    while number != 0:
        reminder = number % 10
        number = number // 10
        result = result * 10 + reminder

    return result

number = eval(input('enter a number : '))
result = reverse_num(number)
print('the reversed number is - {}'.format(result))



#OUTPUT :enter a number : 1234
the reversed number is - 4321
