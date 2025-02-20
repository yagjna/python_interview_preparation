
def fibonacci_series(n):
    # Initialize the first two numbers of the series
    a = 0
    b = 1
    series = [a, b]

    # Generate the Fibonacci series up to n terms
    for _ in range(n-2):
        ans = a + b
        series.append(ans)
        a = b
        b = ans

    return series


# Input: Number of terms
num_terms = int(input("Enter the number of terms: "))
result = fibonacci_series(num_terms)

print('{}'.format(result))

file_name = '28-01-2025'

with open(file_name, 'a') as fh:
    fh.write('fabnocci series : \n')
    fh.write(str(result) + '\n')

print('the file is added to - {}'.format(file_name))
