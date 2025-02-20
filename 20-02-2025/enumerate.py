
# a list of tuples with enumerate

def tuples(days):
    for x,y in enumerate(days):
        print("{}- {}".format(x,y))

days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
result = tuples(days)

file_name = '28-01-2025'

with open(file_name, 'a') as fh:
    fh.write('days : \n')
    fh.write(str((result)) + '\n')

print('the file is added to - {}'.format(file_name))
