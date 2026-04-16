print("Hello, World!")


with open("abc.txt") as file:
    content = file.read()
    print(content)


print("This is a new line of code." + str(len(content)))
