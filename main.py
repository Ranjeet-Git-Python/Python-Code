#Question: Write a Python program that reads the contents of a text file and prints it to the console. Additionally, count the number of characters in the file and print that as well.
print("Hello, World!")
with open("abc.txt") as file:
    content = file.read()
    print(content)

print("done")
print("This is a new line of code." + str(len(content)))
