#Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.



def get_count(sentence):
    # Initialize a counter for vowels
    count = 0
    # Define vowels
    vowels = 'aeiou'
    # Iterate through each character in the sentence
    for x in sentence:
        if x in vowels:  # Check if the character is a vowel
            count += 1  # Increment the vowel count
    return count

# Input sentence
sentence = 'this is a sentence'
# Get the count of vowels
vowel_count = get_count(sentence)
print('The count of vowels is: {}'.format(vowel_count))




#output: The count of vowels is: 6
