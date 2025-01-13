

def number_triangle(height):
    num = 1

    for x in range(1, height + 1):
        row = ""
        for y in range(x):
            row = row + str(num) + " "
            num = num + 1

        print(row.center(height * 2))


height = int(input("Enter the height of the triangle: "))
number_triangle(height)


#output:
Enter the height of the triangle: 5
    1
   2 3
  4 5 6
7 8 9 10
11 12 13 14 15
