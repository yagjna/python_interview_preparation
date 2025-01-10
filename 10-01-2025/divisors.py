

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))


file_name = "prime_and_divisors.txt"

with open(file_name, 'w') as file:

    for num in range(start, end + 1):
        divisors = []
        for x in range(1, num + 1):
            if num % x == 0:
                divisors.append(x)

        file.write("The divisors of {} are: {}\n".format(num, divisors))

        if len(divisors) == 2:
            result = "The {} is prime".format(num)
            print(result)
            file.write("{}\n".format(result))

print("The results have been saved to '{}'.".format(file_name))

