def pos_negitive(start,end):

    positive = []
    negitive = []

    for x in range(start,end+1):
        if x >= 0:
            positive.append(x)
        else:
            negitive.append(x)
    
    return positive, negitive

start = eval(input('enter a number : '))
end = eval(input('enter a number : '))

positive, negitive = pos_negitive(start, end)

print('the positive numbers are - {}'.format(positive))
print('the negitive numbers are - {}'.format(negitive))



#output :enter a number : -11
enter a number : 11
the positive numbers are - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
the negitive numbers are - [-11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
