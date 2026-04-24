import re

def is_valid_email(email):
    pattern =  r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]{1,}[a-zA-Z0-9]@[a-zA-Z0-9][a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None




