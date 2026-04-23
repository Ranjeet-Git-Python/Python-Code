import re

def get_emails_from_file(file_path):
    # Standard regex pattern for finding emails within a text
    email_pattern = r'[a-zA-Z][a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    try:
        with open(file_path, 'r') as file:
            # Read the entire file content
            content = file.read()
            # Find all matches for the email pattern
            emails = re.findall(email_pattern, content)
            return emails
    except FileNotFoundError:
        return "Error: File not found."

# Usage
file_name = "emails.txt"  # Replace with your actual file name
found_emails = get_emails_from_file(file_name)

print(f"Found {len(found_emails)} emails:")
for email in found_emails:
    print(email)
