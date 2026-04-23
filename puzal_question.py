num_legs = 94
num_heads = 35
for i in range(num_legs+1):
    if 4*i+2*(35-i)==num_legs:
        print(f"number of rabbits {i} and number of checkens {35-i}")