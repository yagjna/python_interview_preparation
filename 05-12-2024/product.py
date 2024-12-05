def product(num1,num2):

    if num1 < num2:
        smaller, larger = num1, num2
    else:
        smaller, larger = num2, num1
    result = 0

    for x in range(smaller):
        result  = result + larger

    return result

num1 = eval(input('enter a number : '))
num2 = eval(input('enter a number : '))
result = product(num1, num2)
print(result)



#output :
enter a number : 3
enter a number : 12
12


enter a number : 5
enter a number : 3
15
