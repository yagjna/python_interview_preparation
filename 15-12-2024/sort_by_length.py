def sort_by_length(arr):
    
    return sorted(arr, key=len)


strings = ["Telescopes", "Glasses", "Eyes", "Monocles"]
sorted_strings = sort_by_length(strings)

print(sorted_strings)



#output;
['Eyes', 'Glasses', 'Monocles', 'Telescopes']
