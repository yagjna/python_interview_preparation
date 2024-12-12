def is_prime(num):
    lst1 = []
    for x in range(1,num+1):
        if num % x == 0:
            lst1.append(x)
            
    return True if len(lst1) == 2 else False

num  = 2
lst1 = is_prime(num)


# output : True
