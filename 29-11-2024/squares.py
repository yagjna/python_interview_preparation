# to create squares of even natural numbers from 1 to 100
def squares_of_even_numbers(start, end):
    squares = []
    for x in range(start, end + 1):  
        if x % 2 == 0:  
            squares.append(x ** 2)  
    return squares

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

result = squares_of_even_numbers(start, end)

print("The squares of even numbers in the range are:", result)





output :
    Enter the start of the range: 1
Enter the end of the range: 10
The squares of even numbers in the range are: [4, 16, 36, 64, 100]
