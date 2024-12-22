def high_and_low(numbers):
    
    string_numbers = numbers.split()
    
    int_numbers = []
    
    for num in string_numbers:
        int_numbers.append(int(num))
    
    numbers = int_numbers

    highest = numbers[0]
    lowest = numbers[0]

    for num in numbers:
        if num > highest:
            highest = num  
        if num < lowest:
            lowest = num  

    result = f"{highest} {lowest}"

  
    return result

numbers = "1 2 3 4 5"
print(high_and_low(numbers))


#output:
5 1
