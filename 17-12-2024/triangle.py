n = eval(input(' enter no.of rows:'))

for x in range(n):
    print(' ' * (n - x - 1), end = ' ')

    for y in range(x + 1):
        print(chr(64 + n - y), end = ' ')

    print()


#output:
 D 
   D C 
  D C B 
 D C B A 
