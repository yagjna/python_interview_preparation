def fizzbuzz(n):
    lst1 = []
    
    for x in range(1, n + 1):  
        if x % 3 == 0 and x % 5 == 0:
            lst1.append('FizzBuzz')  
        elif x % 3 == 0:
            lst1.append('Fizz')  
        elif x % 5 == 0:
            lst1.append('Buzz')  
        else:
            lst1.append(x)  
    return lst1


n = 3
print(fizzbuzz(n))  

n = 5
print(fizzbuzz(n))

n= 15
print(fizzbuzz(n))


#OUTPUT:
[1, 2, 'Fizz']
[1, 2, 'Fizz', 4, 'Buzz']
[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
