
def prime_num(number):
    lst1 = []
    for x in range(1, number + 1):
        if number % x == 0:
            lst1.append(x)

    if len(lst1) == 2:
        return "prime"
    else:
        return 'composite number'

number = eval(input('Enter a number: '))
prime = prime_num(number)

print(prime)


filename = "output_prime_no.py"
with open(filename, "w") as file:
    file.write("Number: {}\n".format(number))
    file.write("Result: {}\n".format(prime))

print("The result has been saved to {}.".format(filename))

