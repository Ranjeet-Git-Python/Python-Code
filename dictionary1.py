scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}
#{'Alice': 82, 'Carol': 91, 'Eve': 73}
print({item[0]:item[1] for item in scores.items() if item[1]>60})
print({key:value for key,value in scores.items() if value>60})