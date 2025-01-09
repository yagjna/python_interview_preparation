
def prime_num(start_num, end_num):
    prime_numbers = []

    for num in range(start_num, end_num + 1):

        factors = []
        for x in range(1, num + 1):
            if num % x == 0:
                factors.append(x)

        if len(factors) == 2:
            prime_numbers.append(num)

    return prime_numbers


start_num = int(input('Enter the start of the range: '))
end_num = int(input('Enter the end of the range: '))

prime_numbers = prime_num(start_num, end_num)

filename = "output_prime_numbers.py"
with open(filename, "w") as file:
    file.write("Prime numbers from {} to {}: {}\n".format(start_num, end_num, prime_numbers))

print("The prime numbers have been saved to '{}'.".format(filename))

