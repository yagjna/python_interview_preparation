

def print_number_diamond(n):

    for x in range(1, n + 1):

        print(" " * (n - x), end="")

        for y in range(1, 2 * x):
            print(y, end="")
        print()


    for x in range(n - 1, 0, -1):
        print(" " * (n - x), end="")
        for y in range(1, 2 * x):
            print(y, end="")
        print()

n = int(input("Enter the size of the diamond: "))
size = print_number_diamond(n)
print('{}'.format(size))

#output:
Enter the size of the diamond: 5
    1
   123
  12345
 1234567
123456789
 1234567
  12345
   123
    1
