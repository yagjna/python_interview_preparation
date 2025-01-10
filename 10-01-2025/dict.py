

d = {100: "my", 200: "name", 300: "yagjna"}

key = int(input("Enter key to find corresponding value: "))

file_name = "output_key_value.txt"

with open(file_name, 'w') as file:
    if key in d:
        result = d[key]
        print(result)
        file.write("Key: {}\nValue: {}\n".format(key, result))
    else:
        result = "Specified key is not there."
        print(result)
        file.write("Key: {}\n{}\n".format(key, result))

print("The result has been saved to '{}'.".format(file_name))

