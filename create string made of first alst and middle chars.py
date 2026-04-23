string2 = "Automation Testing"
first_char = string2[0]
last_char = string2[-1]
len_string = len(string2)
middle_length = int(len_string/2)
middle_char = string2[middle_length]
print(middle_length)
print(f"{first_char}{middle_char}{last_char}")
print(first_char+middle_char+last_char)

#middle three chars
string2 = "Automation testing"
length1 = int(len(string2)/2)
p = string2[length1-1:length1+2]
print(p)