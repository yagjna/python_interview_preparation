def flatten_and_sort(array):

    flattened_array = []
    
    for sublist in array:
        for num in sublist:
            flattened_array.append(num)

    print("Flattened Array:{}".format(flattened_array))
    
    sorted_array = sorted(flattened_array)
    
    print("Sorted Array:{}".format (sorted_array))  
    return sorted_array

array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]

result = flatten_and_sort(array)

print("Final Result:{}".format(result))


#output:
Flattened Array:[3, 2, 1, 4, 6, 5, 9, 7, 8]
Sorted Array:[1, 2, 3, 4, 5, 6, 7, 8, 9]
Final Result:[1, 2, 3, 4, 5, 6, 7, 8, 9]
