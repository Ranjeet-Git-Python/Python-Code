#Case 1: Script run directly
#When you run the file with python file.py, __name__ is "__main__".
# demo_direct.py
def greet():
    print("Hello from demo_direct")

if __name__ == "__main__":
    greet()

#Case 2: Script imported as a module
#When you import the file with import file, __name__ is "file"

# demo_import.py
def greet():
    print("Hello from demo_import")

if __name__ == "__main__":
    greet()

