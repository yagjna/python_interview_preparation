def round_to_next5(n):
    
    if n % 5 == 0:
        return n
    else:
        n = n + (5 - n % 5)
        return n
n  = 2
print(round_to_next5(n))

n = 5
print(round_to_next5(n))

n = 13
print(round_to_next5(n))

n = 7
print(round_to_next5(n))

#output:
5
5
15
10
