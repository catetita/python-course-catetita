
file_content ="hola"

with open("test.txt", "w") as new_file:
    new_file.write(file_content)


with open("test.txt", "r") as new_file:
    print(new_file.read().strip())
