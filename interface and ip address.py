for i in range(2, 101,2):
    interface_name = f'GE{i}'
    ip_addess = f'{i}.{i}.{i}.{i}'
    print(f"interface: {interface_name}, ip_address: {ip_addess}")
    
    # Regular expression pattern for validating email addresses