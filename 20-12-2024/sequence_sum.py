def sequence_sum(begin, end, step):
    
    if begin > end:
        return 0
    return sum(range(begin, end + 1, step))

print(sequence_sum(2, 2, 2))  
print(sequence_sum(2, 6, 2))  
print(sequence_sum(1, 5, 1))  
print(sequence_sum(1, 5, 3))  
print(sequence_sum(6, 2, 2))  

#output: 
2
12
15
5
0
