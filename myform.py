from bottle import post, request
import re
from datetime import datetime

@post('/home', method='post')
def my_form():

    question = request.forms.get('QUEST')
    username = request.forms.get('USERNAME')
    email = request.forms.get('ADRESS')
    

    if not question or not username or not email:
        return "Error: All fields must be filled!"
    

    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        return "Error: Invalid email format!"
    

    current_date = datetime.now().strftime("%Y-%m-%d")
    
    return f"Thanks, {username}! The answer will be sent to {email}. Access Date: {current_date}"
