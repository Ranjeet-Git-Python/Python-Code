# Heart Rate Meter
import array

heart_rate = array.array("i",[])
n = int(input(" Enter numer of heart rate reading: "))
for i in range(n):
    heart_rate_reading = int(input(f"Enter heart reading {i+1}: "))
    heart_rate.append(heart_rate_reading)

low_heart_rate = 60
High_heart_rate = 100
low_heart_rate_count = 0
High_heart_rate_count = 0
normal_heart_rate_count = 0
for i in heart_rate:
    if i<low_heart_rate:
        low_heart_rate_count +=1
    elif i>High_heart_rate:
        High_heart_rate_count +=1
    else:
        normal_heart_rate_count +=1
print(f"Low heart rate : {low_heart_rate_count}")
print(f"High heart rate : {High_heart_rate_count}")
print(f"Normal heart rate : {normal_heart_rate_count}")


