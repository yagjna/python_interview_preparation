def maskify(cc):
    
    if len(cc) <= 4:
        return cc
    
    num_to_mask = len(cc) - 4
    
    masked_part = '#' * num_to_mask
    
    last_four = cc[-4:]
    
    result = masked_part + last_four
    

    return result

cc = '4556364607935616'
result =  maskify(cc)
print('the result is : {}'.format(result))




#output : the result is : ############5616
