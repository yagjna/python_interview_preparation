or row in range(7):
    for  col in range(5):
        if (row not in {1, 2}) and (col in {0, 4}):
            print('*', end = ' ')
        elif (row == 1) and (col != 2):
            print('*', end = ' ')
        elif (row == 2) and (col in {0, 2, 4}):
            print('*', end = ' ')
        else:
            print(' ', end = ' ')

    print()


#output:
*       *
* *   * *
*   *   *
*       *
*       *
*       *
*       *
