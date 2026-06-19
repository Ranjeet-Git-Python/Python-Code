list1 = [1, 10, 'a', 33]
 
sum=0
 
for i in list1:
    try:
        sum= sum + i
    except TypeError:
        print ("Type error")
    finally:
        print ("iteration complted ", i)
 
print ("sum", sum)

#2nd method
import builtins
list1 = [1, 10, 'a', 33]
total = builtins.sum(x for x in list1 if isinstance(x, (int, float)))
print(total)

# list1 = [1, 10, 'a', 33]
# total = sum(x for x in list1 if isinstance(x, (int, float)))
# print(total)

list1 = [1, 10, 'a', 33]

total = 0

for item in list1:
    try:
        total += int(item)
    except ValueError:
        print(f"'{item}' is not a valid number. Skipping.")

print("Sum =", total)

list1 = [1, 10, 'a', 33]
sum=0 
for i in list1:
    try:
        sum= sum + i
    except TypeError:
        print ("Type error")

print ("sum", sum)

