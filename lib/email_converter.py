import re

def clean_email(email: str):
    prefix = email.split('@')[0]
    username = re.sub(r'[^a-zA-Z0-9]', '', prefix)
    
    return username
    