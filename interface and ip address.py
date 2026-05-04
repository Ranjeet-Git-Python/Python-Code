#Question: Create a loop to generate interface names and corresponding IP addresses in the format "GE{number}" and "{number}.{number}.{number}.{number}", where the number ranges from 2 to 100 with a step of 2. Print the generated interface names and IP addresses.
for i in range(2, 101,2):
    interface_name = f'GE{i}'
    ip_addess = f'{i}.{i}.{i}.{i}'
    print(f"interface: {interface_name}, ip_address: {ip_addess}")
    
    # Regular expression pattern for validating email addresses