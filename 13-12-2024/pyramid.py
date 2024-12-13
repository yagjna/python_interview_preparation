def pyramid_patterns(rows): 
    for i in range(1, rows + 1):
         print(" " * (rows - i) + "*" * (2 * i - 1))

rows = eval(input('enter number of rows : '))
pyramid_patterns(rows)


#output :
enter number of rows : 5
    *
   ***
  *****
 *******
*********
