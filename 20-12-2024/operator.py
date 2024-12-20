def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b
    else:
        return "Invalid operator"


print(arithmetic(5, 2, "add"))       
print(arithmetic(5, 2, "subtract"))  
print(arithmetic(5, 2, "multiply"))  
print(arithmetic(5, 2, "divide"))   
print(arithmetic(5, 2, "modulo"))    


#output :
7
3
10
2.5
Invalid operator
