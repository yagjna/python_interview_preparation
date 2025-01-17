
def substring_str(str1, substring):
    if substring in str1:
        return 'substring is present'
    else:
        return 'substring is not present'

str1 = 'this is a elephant'
substring = 'elephant'
common = substring_str(str1, substring)

print(common)

str1 = 'this is a elephant'
substring = 'z'
common = substring_str(str1, substring)

print(common)

#output:
substring is present
substring is not present
