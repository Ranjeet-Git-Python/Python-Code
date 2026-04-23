'''A namespace in Python is a container that holds a
collection of names (identifiers) mapped to objects. 
It prevents naming conflicts and organizes code'''

import array
for name in array.__dict__:
    print(name)

print(array.__name__)