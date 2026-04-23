
import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    return False


email = "_abcranje_rt26@yahoo.com"
print(is_valid_email(email))

# 2nd method
def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    return False
email = "user@example.com"
print(is_valid_email(email))

# 3rd Method
def is_valid_email(email):
    if email.count("@") == 1 and email.count(".") >= 1:
        return True
    return False
email = "user@example.com"
print(is_valid_email(email))

# 4th method
def is_valid_email(email):
    if email.startswith("@") or email.startswith("_") or email.startswith(".") or email.endswith("@") or email.endswith("."):
        return False
    if "@" in email and "." in email:
        return True
    return False
email = "_user@example.com"
print(is_valid_email(email))
