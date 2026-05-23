#Question 8. Sort a list of strings in alphabetical order and join them back into a single string with a comma separator.
str1 = "without,hello,bag,world"
l1=str1.split(",")
l1.sort()
print(",".join(l1))