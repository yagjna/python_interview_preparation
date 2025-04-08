def even_odd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
number = eval(input('enter a number : '))
print(even_odd(number))

'''output:enter a number : 7
   odd
enter a number : 6
even'''
