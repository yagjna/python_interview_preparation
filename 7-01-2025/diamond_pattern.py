
n = 5

for row in range(n):
    for col in range(n - row - 1):
        print(' ', end=' ')
    for col in range(2 * row + 1):
        print('*', end=' ')
    print()


for row in range(n - 2, -1, -1):
    for col in range(n - row - 1):
        print(' ', end=' ')
    for col in range(2 * row + 1):
        print('*', end=' ')
    print()



#output:
   *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

