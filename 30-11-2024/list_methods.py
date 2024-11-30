f
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
def list_methods(fruits):
    print("The fruits are: {}".format(fruits))

    # using append to add an element
    fruits.append('cherry')
    print('After append: {}'.format(fruits))

    # using extend to add multiple elements
    fruits.extend(['berry', 'avocado'])  # Pass elements as a list
    print('After extend: {}'.format(fruits))

    # using insert to insert an element in a particular place
    fruits.insert(1, 'blueberry')
    print('After insert: {}'.format(fruits))

fruits = ['apple', 'banana']
list_methods(fruits)




#output :The fruits are: ['apple', 'banana']
After append: ['apple', 'banana', 'cherry']
After extend: ['apple', 'banana', 'cherry', 'berry', 'avocado']
After insert: ['apple', 'blueberry', 'banana', 'cherry', 'berry', 'avocado']
