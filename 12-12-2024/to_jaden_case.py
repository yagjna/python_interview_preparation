
def to_jaden_case(string):
    str1 = string.split(' ')
    lst1 = []
    for x in str1:
        x = x.capitalize()
        lst1.append(x)

    return ' '.join(lst1)

string = "How can mirrors be real if our eyes aren't real"
upper_case = to_jaden_case(string)

print(upper_case)



#output :How Can Mirrors Be Real If Our Eyes Aren't Rea
