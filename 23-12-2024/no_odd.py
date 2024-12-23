def no_odds(values):
    
    lst1 = []
    
    for x in values:
        if x % 2 != 0:
            lst1.append(x)
            
    return lst1

values = [1, 2, 3, 4, 5]
print(no_odds(values))
        
    # Return list of only even values
    

#output:
[1, 3, 5]
