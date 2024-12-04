def substring_freq(str1):

    freq = {}
    length = len(str1)

    for x in range(length):
        for y in range(x+1,length+1):
            substring = str1[x:y]
        if substring in freq:
            freq[substring] = freq[substring] +1
        else:
            freq[substring] = 1

    
    for substring, count in freq.items():
        print(f"'{substring}': {count}")
str1 = 'ababa'
substring_freq(str1)




#output: 
'ababa': 1
'baba': 1
'aba': 1
'ba': 1
'a': 1
