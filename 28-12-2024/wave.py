def wave(word):
    result = []  
    
    for i in range(len(word)):
        if word[i].isalpha():  
            wave_version = word[:i] + word[i].upper() + word[i+1:]
            result.append(wave_version)
    
    return result


word = "hello"
print(wave(word))  


#output:
['Hello', 'hEllo', 'heLlo', 'helLo', 'hellO']
