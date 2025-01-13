
def alphabet_triangle(height):
    for x in range(1, height + 1):
        row = ""
        for y in range(x):
            row = row + chr(65 + y) + " "
        print(row.center(height * 2))


height = int(input("Enter the height of the triangle: "))
alphabet_triangle(height)


#output:
Enter the height of the triangle: 5
    A
   A B
  A B C
 A B C D
A B C D E
