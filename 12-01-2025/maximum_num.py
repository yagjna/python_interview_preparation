
def maximum(num):
    return max(num)

num = [1, 81, 77]
print(maximum(num))

file_name = 'maximum.txt'
with open (file_name, 'w') as fh:
    fh.write('maximum number : {}\n'.format(num))

print("The result has been saved to {}.".format(file_name))
