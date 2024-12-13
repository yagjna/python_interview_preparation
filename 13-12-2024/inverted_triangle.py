def inverted_triangle(rows):
    for i in range(rows, 0, -1):
        # to print spaces
        print(' ' * (rows - i), end='')
        print('* ' * i)

rows = int(input("Enter the number of rows: "))
inverted_triangle(rows)


#output :
Enter the number of rows: 6
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
